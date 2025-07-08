"""
Configuration file for AI Tutor application
Contains API keys, settings, and configuration parameters
"""

import os
from typing import Dict, List

# Application Settings
APP_CONFIG = {
    "title": "AI Tutor for Special Needs Learners",
    "version": "1.0.0",
    "debug": True,
    "database_name": "ai_tutor.db"
}

# Free API Configurations
API_CONFIG = {
    # Hugging Face (Free Tier)
    "huggingface": {
        "api_url": "https://api-inference.huggingface.co/models/",
        "token": os.getenv("HUGGINGFACE_TOKEN", ""),  # Set your token in environment
        "models": {
            "text_generation": "microsoft/DialoGPT-medium",
            "question_answering": "distilbert-base-cased-distilled-squad",
            "text_classification": "cardiffnlp/twitter-roberta-base-emotion"
        }
    },
    
    # OpenAI (Free Credits)
    "openai": {
        "api_key": os.getenv("OPENAI_API_KEY", ""),
        "model": "gpt-3.5-turbo",
        "max_tokens": 150
    },
    
    # Google Gemini (Free Tier)
    "gemini": {
        "api_key": os.getenv("GEMINI_API_KEY", ""),
        "model": "gemini-pro"
    },
    
    # Text-to-Speech APIs
    "tts": {
        "responsivevoice": {
            "base_url": "https://responsivevoice.org/responsivevoice/getvoice.php",
            "voice": "UK English Female",
            "rate": 0.5,
            "pitch": 0.5,
            "volume": 1
        },
        "google_tts": {
            "api_key": os.getenv("GOOGLE_TTS_API_KEY", ""),
            "language": "en-US",
            "voice": "en-US-Wavenet-F"
        }
    }
}

# Learning Content Configuration
LEARNING_CONFIG = {
    "subjects": [
        "Reading & Language",
        "Mathematics",
        "Social Skills",
        "Science Basics",
        "Creative Arts",
        "Life Skills",
        "Physical Education"
    ],
    
    "difficulty_levels": [
        "Beginner",
        "Intermediate", 
        "Advanced"
    ],
    
    "special_needs_categories": [
        "Autism Spectrum Disorder",
        "ADHD",
        "Dyslexia",
        "Intellectual Disability",
        "Down Syndrome",
        "Cerebral Palsy",
        "Learning Disabilities",
        "Sensory Impairments",
        "Other",
        "No specific needs"
    ],
    
    "learning_preferences": [
        "Visual Learning",
        "Audio Learning", 
        "Hands-on Activities",
        "Repetition",
        "Short Sessions",
        "Gamification",
        "Social Learning",
        "Self-paced",
        "Structured Learning"
    ]
}

# Accessibility Configuration
ACCESSIBILITY_CONFIG = {
    "themes": {
        "default": {
            "background": "#ffffff",
            "text": "#333333",
            "primary": "#667eea",
            "secondary": "#764ba2"
        },
        "high_contrast": {
            "background": "#000000",
            "text": "#ffffff", 
            "primary": "#ffff00",
            "secondary": "#00ffff"
        },
        "large_text": {
            "font_size_multiplier": 1.5,
            "line_height_multiplier": 1.6
        }
    },
    
    "tts_settings": {
        "default_speed": 0.8,
        "speed_range": [0.5, 2.0],
        "default_voice": "female",
        "supported_languages": ["en-US", "en-GB", "es-ES", "fr-FR"]
    }
}

# Gamification Configuration
GAMIFICATION_CONFIG = {
    "points_system": {
        "lesson_completion": 10,
        "quiz_perfect": 20,
        "quiz_good": 15,
        "quiz_attempt": 5,
        "daily_streak": 5,
        "achievement_unlock": 25
    },
    
    "achievements": [
        {
            "id": "first_lesson",
            "name": "First Steps",
            "description": "Complete your first lesson",
            "icon": "🎯",
            "points_required": 10
        },
        {
            "id": "quiz_master",
            "name": "Quiz Master", 
            "description": "Score 100% on 5 quizzes",
            "icon": "🏆",
            "points_required": 100
        },
        {
            "id": "week_streak",
            "name": "Dedicated Learner",
            "description": "Learn for 7 days in a row",
            "icon": "🔥",
            "points_required": 35
        },
        {
            "id": "multi_subject",
            "name": "Well Rounded",
            "description": "Complete lessons in 3 different subjects",
            "icon": "🌟",
            "points_required": 50
        }
    ],
    
    "levels": {
        "points_per_level": 100,
        "max_level": 50,
        "level_rewards": {
            5: "Bronze Badge",
            10: "Silver Badge", 
            20: "Gold Badge",
            35: "Platinum Badge",
            50: "Diamond Badge"
        }
    }
}

# Database Configuration
DATABASE_CONFIG = {
    "tables": {
        "users": {
            "columns": [
                "id INTEGER PRIMARY KEY AUTOINCREMENT",
                "username TEXT UNIQUE NOT NULL",
                "password_hash TEXT NOT NULL", 
                "name TEXT NOT NULL",
                "age INTEGER",
                "learning_needs TEXT",
                "preferences TEXT",
                "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
            ]
        },
        "learning_sessions": {
            "columns": [
                "id INTEGER PRIMARY KEY AUTOINCREMENT",
                "user_id INTEGER",
                "subject TEXT",
                "activity_type TEXT",
                "score INTEGER",
                "duration INTEGER",
                "completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
                "FOREIGN KEY (user_id) REFERENCES users (id)"
            ]
        },
        "progress": {
            "columns": [
                "id INTEGER PRIMARY KEY AUTOINCREMENT",
                "user_id INTEGER", 
                "subject TEXT",
                "skill TEXT",
                "level INTEGER DEFAULT 1",
                "points INTEGER DEFAULT 0",
                "last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
                "FOREIGN KEY (user_id) REFERENCES users (id)"
            ]
        },
        "achievements": {
            "columns": [
                "id INTEGER PRIMARY KEY AUTOINCREMENT",
                "user_id INTEGER",
                "achievement_id TEXT",
                "earned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP",
                "FOREIGN KEY (user_id) REFERENCES users (id)"
            ]
        }
    }
}

# Content Templates
CONTENT_TEMPLATES = {
    "lesson_intro": [
        "Welcome to today's lesson on {topic}! Let's learn something amazing together! 🌟",
        "Ready to explore {topic}? This is going to be fun! 🎉", 
        "Today we're diving into {topic}. You're going to do great! 💪"
    ],
    
    "encouragement": [
        "You're doing fantastic! Keep up the great work! 🌟",
        "Amazing progress! I'm so proud of you! 🎉",
        "You're a superstar learner! Keep going! ⭐",
        "Excellent effort! Every step counts! 👏"
    ],
    
    "help_prompts": [
        "Need help? I'm here for you! What would you like to know? 🤗",
        "Stuck on something? Let's figure it out together! 💭",
        "Questions are great! What can I help explain? 🧠"
    ]
}

# Error Messages
ERROR_MESSAGES = {
    "api_error": "Oops! Something went wrong. Let's try again! 🔄",
    "network_error": "Having trouble connecting. Please check your internet! 🌐",
    "auth_error": "Login information doesn't match. Please try again! 🔐",
    "validation_error": "Please fill in all required fields! ✏️"
}

# Success Messages  
SUCCESS_MESSAGES = {
    "lesson_complete": "Fantastic! Lesson completed! 🎉",
    "quiz_perfect": "Perfect score! You're amazing! 🏆", 
    "progress_saved": "Progress saved! Keep up the great work! 💾",
    "achievement_unlocked": "New achievement unlocked! 🏅"
}