<template>
  <section id="platform" class="platform-section">
    <div class="container">
      <div class="section-header">
        <h2>Learning Platform</h2>
        <p>Two specialized portals designed for different user needs</p>
      </div>
      
      <div class="platform-grid">
        <div class="platform-card educator-portal">
          <div class="platform-header">
            <div class="platform-icon">👨‍🏫</div>
            <h3>Educator Portal</h3>
            <p>Comprehensive tools for teachers and specialists</p>
          </div>
          
          <div class="platform-features">
            <div class="platform-feature">
              <span class="feature-icon">📚</span>
              <div class="feature-content">
                <h4>Lesson Planning Tools</h4>
                <p>AI-assisted curriculum development with special needs adaptations</p>
              </div>
            </div>
            <div class="platform-feature">
              <span class="feature-icon">📖</span>
              <div class="feature-content">
                <h4>Resource Library</h4>
                <p>Extensive collection of adaptive learning materials and assessments</p>
              </div>
            </div>
            <div class="platform-feature">
              <span class="feature-icon">📊</span>
              <div class="feature-content">
                <h4>Progress Tracking</h4>
                <p>Real-time analytics and insights on student development</p>
              </div>
            </div>
            <div class="platform-feature">
              <span class="feature-icon">👥</span>
              <div class="feature-content">
                <h4>Collaboration Hub</h4>
                <p>Connect with other educators and share best practices</p>
              </div>
            </div>
          </div>
          
          <button class="btn btn-primary" @click="openPortal('educator')">Access Educator Portal</button>
        </div>
        
        <div class="platform-card student-portal">
          <div class="platform-header">
            <div class="platform-icon">🎓</div>
            <h3>Personalized Learning Portal</h3>
            <p>Adaptive learning experience for students</p>
          </div>
          
          <div class="platform-features">
            <div class="platform-feature">
              <span class="feature-icon">🎯</span>
              <div class="feature-content">
                <h4>Adaptive Content</h4>
                <p>Lessons that adjust to individual learning styles and pace</p>
              </div>
            </div>
            <div class="platform-feature">
              <span class="feature-icon">🎮</span>
              <div class="feature-content">
                <h4>Interactive Activities</h4>
                <p>Engaging games and exercises tailored to specific needs</p>
              </div>
            </div>
            <div class="platform-feature">
              <span class="feature-icon">🏆</span>
              <div class="feature-content">
                <h4>Achievement System</h4>
                <p>Motivation through personalized rewards and progress tracking</p>
              </div>
            </div>
            <div class="platform-feature">
              <span class="feature-icon">🤝</span>
              <div class="feature-content">
                <h4>Support Network</h4>
                <p>Connect with peers and mentors in safe, moderated spaces</p>
              </div>
            </div>
          </div>
          
          <button class="btn btn-secondary" @click="openPortal('student')">Start Learning</button>
        </div>
      </div>
      
      <div class="platform-demo">
        <h3>See Our Platform in Action</h3>
        <div class="demo-container">
          <div class="demo-placeholder">
            <div class="demo-icon">🎥</div>
            <p>Interactive Platform Demo</p>
            <button class="btn btn-demo">Watch Demo</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Login Modal -->
    <LoginModal 
      :isOpen="showLoginModal" 
      :portalType="selectedPortalType"
      @close="closeLoginModal"
      @login-success="handleLoginSuccess"
    />
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useAuthStore } from '../stores/authStore'
import LoginModal from './LoginModal.vue'

const authStore = useAuthStore()
const showLoginModal = ref(false)
const selectedPortalType = ref<'educator' | 'student'>('educator')

const emit = defineEmits<{
  'show-portal': [type: 'educator' | 'student']
}>()

const openPortal = (type: 'educator' | 'student') => {
  if (authStore.isAuthenticated.value) {
    // User is already logged in, show the portal directly
    emit('show-portal', type)
  } else {
    // User needs to log in first
    selectedPortalType.value = type
    showLoginModal.value = true
  }
}

const closeLoginModal = () => {
  showLoginModal.value = false
}

const handleLoginSuccess = (type: 'educator' | 'student') => {
  showLoginModal.value = false
  emit('show-portal', type)
}
</script>

<style scoped>
.platform-section {
  padding: 6rem 0;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
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
  margin-bottom: 1rem;
}

.section-header p {
  font-size: 1.25rem;
  opacity: 0.9;
  max-width: 600px;
  margin: 0 auto;
}

.platform-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  margin-bottom: 4rem;
}

.platform-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 30px;
  padding: 3rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
}

.platform-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 30px 60px rgba(0,0,0,0.2);
}

.platform-header {
  text-align: center;
  margin-bottom: 3rem;
}

.platform-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.platform-header h3 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.platform-header p {
  opacity: 0.9;
  font-size: 1.1rem;
}

.platform-features {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  margin-bottom: 3rem;
}

.platform-feature {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.feature-icon {
  font-size: 1.5rem;
  flex-shrink: 0;
  margin-top: 0.25rem;
}

.feature-content h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  font-weight: 600;
}

.feature-content p {
  margin: 0;
  opacity: 0.8;
  line-height: 1.5;
}

.btn {
  padding: 1rem 2rem;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;
  text-align: center;
}

.btn-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.btn-secondary {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
  color: white;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

.platform-demo {
  text-align: center;
  margin-top: 4rem;
}

.platform-demo h3 {
  font-size: 2rem;
  margin-bottom: 2rem;
}

.demo-container {
  max-width: 600px;
  margin: 0 auto;
}

.demo-placeholder {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 3rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.demo-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.demo-placeholder p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.btn-demo {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 2px solid white;
  width: auto;
  padding: 1rem 3rem;
}

@media (max-width: 768px) {
  .platform-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .platform-card {
    padding: 2rem;
  }
  
  .section-header h2 {
    font-size: 2rem;
  }
  
  .platform-header h3 {
    font-size: 1.5rem;
  }
}
</style>