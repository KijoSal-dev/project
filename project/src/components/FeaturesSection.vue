<template>
  <section id="features" class="features-section">
    <div class="container">
      <div class="section-header">
        <h2>AI-Powered Features</h2>
        <p>Cutting-edge technology designed specifically for special needs education</p>
      </div>
      
      <div class="features-grid">
        <div class="feature-card" v-for="feature in features" :key="feature.id">
          <div class="feature-icon">{{ feature.icon }}</div>
          <h3>{{ feature.title }}</h3>
          <p>{{ feature.description }}</p>
          <div class="feature-tags">
            <span class="tag" v-for="tag in feature.tags" :key="tag">{{ tag }}</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const features = ref([
  {
    id: 1,
    icon: '🎯',
    title: 'Personalized Learning Paths',
    description: 'AI-tailored lessons based on individual learning pace and style, adapting in real-time to student needs.',
    tags: ['AI', 'Adaptive', 'Individual']
  },
  {
    id: 2,
    icon: '🎨',
    title: 'Multimodal Content Delivery',
    description: 'Visual, auditory, and interactive content options to accommodate different learning preferences.',
    tags: ['Visual', 'Audio', 'Interactive']
  },
  {
    id: 3,
    icon: '🎤',
    title: 'Speech-to-Text & Text-to-Speech',
    description: 'Advanced communication tools for users with speech or reading difficulties.',
    tags: ['Accessibility', 'Communication', 'Voice']
  },
  {
    id: 4,
    icon: '😊',
    title: 'Emotion Recognition',
    description: 'AI detects frustration or confusion and adjusts support in real-time to maintain engagement.',
    tags: ['AI', 'Emotion', 'Support']
  },
  {
    id: 5,
    icon: '📅',
    title: 'Routine & Schedule Assistants',
    description: 'Visual calendars with reminders to help students maintain structure and routine.',
    tags: ['Organization', 'Visual', 'Routine']
  },
  {
    id: 6,
    icon: '🎮',
    title: 'Gamified Learning Modules',
    description: 'Motivation through rewards and interactive challenges tailored to each student.',
    tags: ['Gamification', 'Motivation', 'Rewards']
  },
  {
    id: 7,
    icon: '📊',
    title: 'Behavior Tracking',
    description: 'AI logs progress and patterns to inform caregivers and teachers about student development.',
    tags: ['Analytics', 'Progress', 'Insights']
  },
  {
    id: 8,
    icon: '👨‍👩‍👧‍👦',
    title: 'Parent/Teacher Dashboards',
    description: 'Comprehensive insights, alerts, and recommended support strategies for educators and families.',
    tags: ['Dashboard', 'Family', 'Teachers']
  },
  {
    id: 9,
    icon: '♿',
    title: 'Accessible Design Features',
    description: 'High contrast mode, adjustable font sizes, and keyboard navigation for universal access.',
    tags: ['Accessibility', 'Universal', 'Design']
  },
  {
    id: 10,
    icon: '💬',
    title: 'Social Skills Simulators',
    description: 'AI-driven scenarios to practice communication and social interaction in safe environments.',
    tags: ['Social', 'Practice', 'Safe']
  },
  {
    id: 11,
    icon: '📝',
    title: 'Language Simplification Tools',
    description: 'AI rephrases complex instructions into simpler, more understandable language.',
    tags: ['Language', 'Simplification', 'Clarity']
  },
  {
    id: 12,
    icon: '🎧',
    title: 'Voice Assistant Support',
    description: 'Easy navigation and learning through conversational AI and voice commands.',
    tags: ['Voice', 'Navigation', 'Assistant']
  },
  {
    id: 13,
    icon: '🌐',
    title: 'Real-Time Translation',
    description: 'Helps multilingual learners and caregivers understand content in their preferred language.',
    tags: ['Translation', 'Multilingual', 'Inclusive']
  },
  {
    id: 14,
    icon: '📈',
    title: 'Progressive Difficulty Scaling',
    description: 'AI increases complexity gradually based on learner mastery and confidence levels.',
    tags: ['Adaptive', 'Progressive', 'Mastery']
  },
  {
    id: 15,
    icon: '🛡️',
    title: 'Safe Interaction Spaces',
    description: 'Moderated forums and chatbots for practicing social communication in secure environments.',
    tags: ['Safety', 'Moderated', 'Social']
  }
])
</script>

<style scoped>
.features-section {
  padding: 6rem 0;
  background: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-header h2 {
  font-size: 3rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 1rem;
}

.section-header p {
  font-size: 1.25rem;
  color: #666;
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: all 0.3s ease;
  border: 1px solid #f0f0f0;
}

.feature-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
  display: block;
}

.feature-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 1rem;
}

.feature-card p {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  
  .section-header h2 {
    font-size: 2rem;
  }
  
  .feature-card {
    padding: 1.5rem;
  }
}
</style>