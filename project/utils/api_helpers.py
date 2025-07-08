"""
API Helper functions for integrating with free APIs
"""

import requests
import json
import time
from typing import Dict, List, Optional
import streamlit as st
from config import API_CONFIG

class APIHelper:
    """Helper class for API integrations"""
    
    @staticmethod
    def call_huggingface_api(model_name: str, inputs: str, max_retries: int = 3) -> Optional[Dict]:
        """
        Call Hugging Face Inference API
        
        Args:
            model_name: Name of the model to use
            inputs: Input text for the model
            max_retries: Maximum number of retry attempts
            
        Returns:
            API response or None if failed
        """
        api_url = f"{API_CONFIG['huggingface']['api_url']}{model_name}"
        headers = {"Authorization": f"Bearer {API_CONFIG['huggingface']['token']}"}
        
        payload = {"inputs": inputs}
        
        for attempt in range(max_retries):
            try:
                response = requests.post(api_url, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 503:
                    # Model is loading, wait and retry
                    time.sleep(10)
                    continue
                else:
                    st.error(f"API Error: {response.status_code}")
                    return None
                    
            except requests.exceptions.RequestException as e:
                st.error(f"Network error: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue
                return None
        
        return None
    
    @staticmethod
    def generate_educational_content(topic: str, difficulty: str, special_needs: str = None) -> Dict:
        """
        Generate educational content using AI APIs
        
        Args:
            topic: Subject topic
            difficulty: Difficulty level
            special_needs: Specific learning needs
            
        Returns:
            Generated content dictionary
        """
        # Construct prompt based on parameters
        prompt = f"""
        Create an educational lesson about {topic} for {difficulty} level.
        {f'Adapted for learners with {special_needs}.' if special_needs else ''}
        
        Include:
        1. A clear, simple explanation
        2. 3 learning activities
        3. A helpful tip
        4. Encouraging language
        
        Make it engaging and accessible.
        """
        
        # Try Hugging Face first
        if API_CONFIG['huggingface']['token']:
            result = APIHelper.call_huggingface_api(
                API_CONFIG['huggingface']['models']['text_generation'],
                prompt
            )
            
            if result:
                return APIHelper.parse_generated_content(result, topic, difficulty)
        
        # Fallback to template-based content
        return APIHelper.get_template_content(topic, difficulty, special_needs)
    
    @staticmethod
    def parse_generated_content(api_result: Dict, topic: str, difficulty: str) -> Dict:
        """Parse API result into structured content"""
        try:
            # Extract generated text (format varies by model)
            if isinstance(api_result, list) and len(api_result) > 0:
                generated_text = api_result[0].get('generated_text', '')
            else:
                generated_text = str(api_result)
            
            # Simple parsing (in production, use more sophisticated NLP)
            lines = generated_text.split('\n')
            
            return {
                'title': f"Learning About {topic.title()}",
                'content': generated_text[:500] + "..." if len(generated_text) > 500 else generated_text,
                'activities': [
                    "Interactive exploration",
                    "Hands-on practice", 
                    "Creative expression"
                ],
                'tips': "Take your time and ask questions if you need help!"
            }
            
        except Exception as e:
            st.error(f"Error parsing content: {e}")
            return APIHelper.get_template_content(topic, difficulty)
    
    @staticmethod
    def get_template_content(topic: str, difficulty: str, special_needs: str = None) -> Dict:
        """Fallback template-based content generation"""
        
        content_library = {
            "reading": {
                "beginner": {
                    "title": f"Reading Adventures: {topic}",
                    "content": f"Today we'll explore the wonderful world of {topic}! We'll use pictures, sounds, and fun activities to help you learn. Reading is like going on an adventure - every page takes us somewhere new!",
                    "activities": [
                        "Look at pictures and name what you see",
                        "Practice letter sounds with fun games",
                        "Read simple words together"
                    ],
                    "tips": "Point to each word as you read. Don't worry about mistakes - they help us learn!"
                },
                "intermediate": {
                    "title": f"Story Exploration: {topic}",
                    "content": f"Let's dive deeper into {topic} through exciting stories and activities! We'll build your reading skills while having fun with characters and adventures.",
                    "activities": [
                        "Read short stories and discuss characters",
                        "Answer questions about what happened",
                        "Create your own story ending"
                    ],
                    "tips": "If you don't understand a word, look at the pictures for clues!"
                }
            },
            "math": {
                "beginner": {
                    "title": f"Math Fun: {topic}",
                    "content": f"Math is everywhere around us! Today we'll explore {topic} using objects you can touch and see. We'll count, sort, and play with numbers in fun ways!",
                    "activities": [
                        "Count objects using your fingers or toys",
                        "Sort items by size, color, or shape",
                        "Play number games with visual aids"
                    ],
                    "tips": "Use real objects to help you count - blocks, toys, or even snacks work great!"
                },
                "intermediate": {
                    "title": f"Math Exploration: {topic}",
                    "content": f"Ready for some math challenges? We'll explore {topic} through puzzles, patterns, and problem-solving activities that make math exciting!",
                    "activities": [
                        "Solve word problems step by step",
                        "Find patterns in numbers and shapes",
                        "Use math in real-life situations"
                    ],
                    "tips": "Break big problems into smaller pieces. Take your time and think it through!"
                }
            },
            "social": {
                "beginner": {
                    "title": f"Social Skills: {topic}",
                    "content": f"Learning about {topic} helps us make friends and feel good around others! We'll practice through games, stories, and fun activities.",
                    "activities": [
                        "Practice greetings and conversations",
                        "Learn about different emotions",
                        "Role-play social situations"
                    ],
                    "tips": "Practice with family first, then try with friends. Everyone learns at their own pace!"
                }
            }
        }
        
        # Determine subject category
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ['read', 'story', 'book', 'letter']):
            subject = 'reading'
        elif any(word in topic_lower for word in ['math', 'number', 'count', 'add']):
            subject = 'math'
        elif any(word in topic_lower for word in ['social', 'friend', 'emotion', 'feeling']):
            subject = 'social'
        else:
            subject = 'reading'  # default
        
        # Get content with fallback
        content = content_library.get(subject, {}).get(difficulty.lower(), 
                  content_library['reading']['beginner'])
        
        # Adapt for special needs if specified
        if special_needs and special_needs != "No specific needs":
            content = APIHelper.adapt_for_special_needs(content, special_needs)
        
        return content
    
    @staticmethod
    def adapt_for_special_needs(content: Dict, special_needs: str) -> Dict:
        """Adapt content for specific special needs"""
        
        adaptations = {
            "Autism Spectrum Disorder": {
                "content_suffix": " We'll use clear, simple steps and visual supports to help you succeed.",
                "additional_tip": " Remember: it's okay to take breaks when you need them."
            },
            "ADHD": {
                "content_suffix": " We'll keep activities short and fun with lots of movement and variety!",
                "additional_tip": " Try to find a quiet space and take movement breaks when needed."
            },
            "Dyslexia": {
                "content_suffix": " We'll use lots of pictures, colors, and different ways to show information.",
                "additional_tip": " Don't worry about spelling - focus on understanding and expressing your ideas!"
            },
            "Intellectual Disability": {
                "content_suffix": " We'll go step by step and repeat important ideas to help you learn.",
                "additional_tip": " Take your time - there's no rush! Every small step is progress."
            }
        }
        
        if special_needs in adaptations:
            adaptation = adaptations[special_needs]
            content['content'] += adaptation['content_suffix']
            content['tips'] += adaptation['additional_tip']
        
        return content
    
    @staticmethod
    def generate_quiz_questions(topic: str, difficulty: str, count: int = 3) -> List[Dict]:
        """Generate quiz questions for a topic"""
        
        question_templates = {
            "reading": {
                "beginner": [
                    {
                        "question": "What sound does the letter 'A' make?",
                        "options": ["Ah", "Buh", "Kuh", "Duh"],
                        "correct": 0,
                        "explanation": "The letter A makes the 'Ah' sound, like in 'Apple'!"
                    },
                    {
                        "question": "Which word starts with 'B'?",
                        "options": ["Cat", "Ball", "Dog", "Fish"],
                        "correct": 1,
                        "explanation": "Ball starts with 'B' - B makes the 'Buh' sound!"
                    },
                    {
                        "question": "How many words are in this sentence: 'I like cats'?",
                        "options": ["2", "3", "4", "5"],
                        "correct": 1,
                        "explanation": "Count them: 'I' (1), 'like' (2), 'cats' (3) = 3 words!"
                    }
                ],
                "intermediate": [
                    {
                        "question": "What is a synonym for 'happy'?",
                        "options": ["Sad", "Joyful", "Angry", "Tired"],
                        "correct": 1,
                        "explanation": "Joyful means the same thing as happy!"
                    },
                    {
                        "question": "In the sentence 'The big dog ran fast', what describes the dog?",
                        "options": ["ran", "big", "fast", "the"],
                        "correct": 1,
                        "explanation": "'Big' is an adjective that describes the dog!"
                    }
                ]
            },
            "math": {
                "beginner": [
                    {
                        "question": "What comes after 7?",
                        "options": ["6", "8", "9", "5"],
                        "correct": 1,
                        "explanation": "When counting: 6, 7, 8... So 8 comes after 7!"
                    },
                    {
                        "question": "How many fingers do you have on one hand?",
                        "options": ["4", "5", "6", "3"],
                        "correct": 1,
                        "explanation": "Count your fingers: 1, 2, 3, 4, 5!"
                    },
                    {
                        "question": "What is 2 + 1?",
                        "options": ["2", "3", "4", "1"],
                        "correct": 1,
                        "explanation": "2 + 1 = 3. You can count: 2, then add 1 more!"
                    }
                ],
                "intermediate": [
                    {
                        "question": "What is 15 - 7?",
                        "options": ["7", "8", "9", "6"],
                        "correct": 1,
                        "explanation": "15 - 7 = 8. You can count backwards from 15!"
                    },
                    {
                        "question": "Which number is even?",
                        "options": ["7", "9", "12", "15"],
                        "correct": 2,
                        "explanation": "12 is even because it can be divided by 2 equally!"
                    }
                ]
            }
        }
        
        # Determine subject
        topic_lower = topic.lower()
        if any(word in topic_lower for word in ['math', 'number', 'count']):
            subject = 'math'
        else:
            subject = 'reading'
        
        # Get questions
        questions = question_templates.get(subject, {}).get(difficulty.lower(), 
                   question_templates['reading']['beginner'])
        
        # Return requested number of questions
        return questions[:count] if len(questions) >= count else questions
    
    @staticmethod
    def get_text_to_speech_url(text: str, voice: str = "female") -> str:
        """Generate text-to-speech URL using free services"""
        
        # Clean and encode text
        clean_text = text.replace('\n', ' ').strip()[:500]  # Limit length
        
        # Use ResponsiveVoice (free service)
        tts_config = API_CONFIG['tts']['responsivevoice']
        
        params = {
            't': clean_text,
            'tl': 'en',
            'sv': 'g1' if voice == 'female' else 'g2',
            'vn': '',
            'pitch': tts_config['pitch'],
            'rate': tts_config['rate'],
            'vol': tts_config['volume']
        }
        
        # Build URL
        param_string = '&'.join([f"{k}={requests.utils.quote(str(v))}" for k, v in params.items()])
        return f"{tts_config['base_url']}?{param_string}"
    
    @staticmethod
    def analyze_emotion(text: str) -> Dict:
        """Analyze emotion in text using free APIs"""
        
        if API_CONFIG['huggingface']['token']:
            result = APIHelper.call_huggingface_api(
                API_CONFIG['huggingface']['models']['text_classification'],
                text
            )
            
            if result and isinstance(result, list):
                emotions = {}
                for item in result:
                    if 'label' in item and 'score' in item:
                        emotions[item['label']] = item['score']
                return emotions
        
        # Fallback: simple keyword-based emotion detection
        emotion_keywords = {
            'joy': ['happy', 'excited', 'great', 'awesome', 'love', 'wonderful'],
            'sadness': ['sad', 'upset', 'disappointed', 'down', 'unhappy'],
            'anger': ['angry', 'mad', 'frustrated', 'annoyed', 'irritated'],
            'fear': ['scared', 'afraid', 'worried', 'nervous', 'anxious'],
            'surprise': ['surprised', 'amazed', 'shocked', 'wow', 'incredible']
        }
        
        text_lower = text.lower()
        detected_emotions = {}
        
        for emotion, keywords in emotion_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                detected_emotions[emotion] = score / len(keywords)
        
        return detected_emotions if detected_emotions else {'neutral': 1.0}