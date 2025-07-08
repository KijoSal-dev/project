<template>
  <section id="contribute" class="cta-section">
    <div class="container">
      <div class="cta-content">
        <h2>Join the Movement</h2>
        <p class="cta-subtitle">
          Help us transform special needs education in Kenya. Whether you're an educator, 
          developer, specialist, or simply passionate about inclusive education, there's a place for you.
        </p>
        
        <div class="cta-cards">
          <div class="cta-card" @click="openJoinModal">
            <div class="cta-icon">👨‍🏫</div>
            <h3>Educators</h3>
            <p>Share your expertise and help shape the future of special needs education</p>
            <button class="btn btn-primary">Join as Educator</button>
          </div>
          
          <div class="cta-card" @click="openJoinModal">
            <div class="cta-icon">💻</div>
            <h3>Developers</h3>
            <p>Contribute to our open-source platform and build accessible technology</p>
            <button class="btn btn-primary">Contribute Code</button>
          </div>
          
          <div class="cta-card" @click="openJoinModal">
            <div class="cta-icon">🏥</div>
            <h3>Specialists</h3>
            <p>Provide clinical insights and help us create evidence-based solutions</p>
            <button class="btn btn-primary">Join as Specialist</button>
          </div>
          
          <div class="cta-card" @click="openJoinModal">
            <div class="cta-icon">❤️</div>
            <h3>Supporters</h3>
            <p>Support our mission through donations, partnerships, or spreading awareness</p>
            <button class="btn btn-primary">Support Us</button>
          </div>
        </div>
        
        <div class="cta-newsletter">
          <h3>Stay Updated</h3>
          <p>Get the latest news about our progress and impact</p>
          <form @submit.prevent="subscribeNewsletter" class="newsletter-form">
            <input 
              type="email" 
              placeholder="Enter your email" 
              class="newsletter-input"
              v-model="newsletterEmail"
              required
            >
            <button type="submit" class="btn btn-newsletter">Subscribe</button>
          </form>
          <p v-if="subscriptionMessage" class="subscription-message">{{ subscriptionMessage }}</p>
        </div>
      </div>
    </div>

    <!-- Join Modal -->
    <JoinModal 
      :isOpen="showJoinModal"
      @close="closeJoinModal"
      @role-selected="handleRoleSelection"
    />
  </section>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import JoinModal from './JoinModal.vue'

const showJoinModal = ref(false)
const newsletterEmail = ref('')
const subscriptionMessage = ref('')

const openJoinModal = () => {
  showJoinModal.value = true
}

const closeJoinModal = () => {
  showJoinModal.value = false
}

const handleRoleSelection = (role: string) => {
  console.log('Role selected:', role)
  // Here you would typically redirect to a specific signup flow
  // or show a role-specific form
}

const subscribeNewsletter = () => {
  // Handle newsletter subscription
  console.log('Newsletter subscription:', newsletterEmail.value)
  
  // Simulate API call
  setTimeout(() => {
    subscriptionMessage.value = 'Thank you for subscribing! You\'ll receive updates about our progress.'
    newsletterEmail.value = ''
    
    // Clear message after 5 seconds
    setTimeout(() => {
      subscriptionMessage.value = ''
    }, 5000)
  }, 1000)
}
</script>

<style scoped>
.cta-section {
  padding: 6rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.cta-content {
  text-align: center;
}

.cta-content h2 {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.cta-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  margin-bottom: 4rem;
  opacity: 0.9;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.cta-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 4rem;
}

.cta-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.3s ease;
  cursor: pointer;
}

.cta-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

.cta-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.cta-card h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.cta-card p {
  opacity: 0.9;
  margin-bottom: 2rem;
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
}

.btn-primary {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
}

.cta-newsletter {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 3rem;
  border: 1px solid rgba(255, 255, 255, 0.2);
  max-width: 600px;
  margin: 0 auto;
}

.cta-newsletter h3 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.cta-newsletter p {
  opacity: 0.9;
  margin-bottom: 2rem;
}

.newsletter-form {
  display: flex;
  gap: 1rem;
  max-width: 400px;
  margin: 0 auto;
}

.newsletter-input {
  flex: 1;
  padding: 1rem;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  background: rgba(255, 255, 255, 0.9);
  color: #333;
}

.newsletter-input::placeholder {
  color: #666;
}

.btn-newsletter {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
  color: white;
  white-space: nowrap;
  width: auto;
}

.subscription-message {
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .cta-content h2 {
    font-size: 2rem;
  }
  
  .cta-subtitle {
    font-size: 1.1rem;
  }
  
  .cta-cards {
    grid-template-columns: 1fr;
  }
  
  .newsletter-form {
    flex-direction: column;
  }
  
  .btn-newsletter {
    width: 100%;
  }
}
</style>