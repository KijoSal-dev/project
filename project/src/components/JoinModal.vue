<template>
  <div v-if="isOpen" class="modal-overlay" @click="closeModal">
    <div class="modal-content" @click.stop>
      <button class="modal-close" @click="closeModal">&times;</button>
      
      <div class="modal-header">
        <h2>Join the Movement</h2>
        <p>Choose how you'd like to contribute to transforming special needs education in Kenya</p>
      </div>
      
      <div class="join-options">
        <div class="join-card" @click="selectRole('educator')">
          <div class="card-icon">👨‍🏫</div>
          <h3>Educator</h3>
          <p>Share your expertise and help shape the future of special needs education</p>
          <ul class="benefits-list">
            <li>Access to advanced teaching tools</li>
            <li>Professional development resources</li>
            <li>Community of expert educators</li>
            <li>Impact tracking and analytics</li>
          </ul>
          <button class="btn btn-primary">Join as Educator</button>
        </div>
        
        <div class="join-card" @click="selectRole('developer')">
          <div class="card-icon">💻</div>
          <h3>Developer</h3>
          <p>Contribute to our open-source platform and build accessible technology</p>
          <ul class="benefits-list">
            <li>Open source contribution</li>
            <li>Cutting-edge AI/ML projects</li>
            <li>Accessibility-focused development</li>
            <li>Global impact through code</li>
          </ul>
          <button class="btn btn-primary">Contribute Code</button>
        </div>
        
        <div class="join-card" @click="selectRole('specialist')">
          <div class="card-icon">🏥</div>
          <h3>Specialist</h3>
          <p>Provide clinical insights and help us create evidence-based solutions</p>
          <ul class="benefits-list">
            <li>Clinical research opportunities</li>
            <li>Evidence-based solution design</li>
            <li>Professional networking</li>
            <li>Continuing education credits</li>
          </ul>
          <button class="btn btn-primary">Join as Specialist</button>
        </div>
        
        <div class="join-card" @click="selectRole('supporter')">
          <div class="card-icon">❤️</div>
          <h3>Supporter</h3>
          <p>Support our mission through donations, partnerships, or spreading awareness</p>
          <ul class="benefits-list">
            <li>Regular impact updates</li>
            <li>Community events access</li>
            <li>Recognition programs</li>
            <li>Tax-deductible donations</li>
          </ul>
          <button class="btn btn-primary">Support Us</button>
        </div>
      </div>
      
      <div class="modal-footer">
        <p>Not sure which role fits you? <button @click="showContactForm = true" class="link-button">Contact us</button> and we'll help you find the perfect way to contribute.</p>
      </div>
    </div>
  </div>

  <!-- Contact Form Modal -->
  <div v-if="showContactForm" class="modal-overlay" @click="closeContactForm">
    <div class="modal-content contact-modal" @click.stop>
      <button class="modal-close" @click="closeContactForm">&times;</button>
      
      <div class="modal-header">
        <h2>Get in Touch</h2>
        <p>Tell us about yourself and how you'd like to contribute</p>
      </div>
      
      <form @submit.prevent="submitContactForm" class="contact-form">
        <div class="form-row">
          <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" v-model="contactForm.firstName" required>
          </div>
          <div class="form-group">
            <label for="lastName">Last Name</label>
            <input type="text" id="lastName" v-model="contactForm.lastName" required>
          </div>
        </div>
        
        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" v-model="contactForm.email" required>
        </div>
        
        <div class="form-group">
          <label for="phone">Phone Number (Optional)</label>
          <input type="tel" id="phone" v-model="contactForm.phone">
        </div>
        
        <div class="form-group">
          <label for="organization">Organization/Institution (Optional)</label>
          <input type="text" id="organization" v-model="contactForm.organization">
        </div>
        
        <div class="form-group">
          <label for="interests">Areas of Interest</label>
          <div class="checkbox-group">
            <label class="checkbox-label">
              <input type="checkbox" v-model="contactForm.interests" value="education">
              <span class="checkmark"></span>
              Special Needs Education
            </label>
            <label class="checkbox-label">
              <input type="checkbox" v-model="contactForm.interests" value="technology">
              <span class="checkmark"></span>
              Technology Development
            </label>
            <label class="checkbox-label">
              <input type="checkbox" v-model="contactForm.interests" value="research">
              <span class="checkmark"></span>
              Research & Clinical Work
            </label>
            <label class="checkbox-label">
              <input type="checkbox" v-model="contactForm.interests" value="funding">
              <span class="checkmark"></span>
              Funding & Partnerships
            </label>
            <label class="checkbox-label">
              <input type="checkbox" v-model="contactForm.interests" value="advocacy">
              <span class="checkmark"></span>
              Advocacy & Awareness
            </label>
          </div>
        </div>
        
        <div class="form-group">
          <label for="message">Tell us about yourself and how you'd like to contribute</label>
          <textarea 
            id="message" 
            v-model="contactForm.message" 
            rows="4" 
            placeholder="Share your background, experience, and ideas for how you'd like to help transform special needs education in Kenya..."
            required
          ></textarea>
        </div>
        
        <div class="form-group">
          <label class="checkbox-label">
            <input type="checkbox" v-model="contactForm.newsletter" checked>
            <span class="checkmark"></span>
            Subscribe to our newsletter for updates on the project
          </label>
        </div>
        
        <button type="submit" class="btn btn-primary submit-btn">Send Message</button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

interface Emits {
  (e: 'close'): void
  (e: 'role-selected', role: string): void
}

const props = defineProps<{
  isOpen: boolean
}>()

const emit = defineEmits<Emits>()

const showContactForm = ref(false)

const contactForm = ref({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  organization: '',
  interests: [] as string[],
  message: '',
  newsletter: true
})

const closeModal = () => {
  emit('close')
}

const closeContactForm = () => {
  showContactForm.value = false
}

const selectRole = (role: string) => {
  emit('role-selected', role)
  closeModal()
}

const submitContactForm = () => {
  // Handle form submission
  console.log('Contact form submitted:', contactForm.value)
  
  // Show success message (you can implement a toast notification here)
  alert('Thank you for your interest! We\'ll get back to you within 24 hours.')
  
  // Reset form and close modal
  contactForm.value = {
    firstName: '',
    lastName: '',
    email: '',
    phone: '',
    organization: '',
    interests: [],
    message: '',
    newsletter: true
  }
  
  closeContactForm()
  closeModal()
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  padding: 1rem;
}

.modal-content {
  background: white;
  border-radius: 20px;
  padding: 2rem;
  width: 100%;
  max-width: 1000px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
}

.contact-modal {
  max-width: 600px;
}

.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #666;
  transition: color 0.3s ease;
  z-index: 1;
}

.modal-close:hover {
  color: #333;
}

.modal-header {
  text-align: center;
  margin-bottom: 3rem;
}

.modal-header h2 {
  color: #333;
  margin-bottom: 1rem;
  font-size: 2.5rem;
}

.modal-header p {
  color: #666;
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
}

.join-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 3rem;
}

.join-card {
  background: #f8f9fa;
  border-radius: 20px;
  padding: 2rem;
  text-align: center;
  transition: all 0.3s ease;
  cursor: pointer;
  border: 2px solid transparent;
}

.join-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.1);
  border-color: #667eea;
}

.card-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.join-card h3 {
  margin: 0 0 1rem 0;
  color: #333;
  font-size: 1.5rem;
}

.join-card p {
  margin: 0 0 1.5rem 0;
  color: #666;
  line-height: 1.5;
}

.benefits-list {
  text-align: left;
  margin: 1.5rem 0;
  padding: 0;
  list-style: none;
}

.benefits-list li {
  padding: 0.5rem 0;
  color: #555;
  position: relative;
  padding-left: 1.5rem;
}

.benefits-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #28a745;
  font-weight: bold;
}

.join-card .btn {
  width: 100%;
  margin-top: 1rem;
}

.modal-footer {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid #e0e0e0;
}

.modal-footer p {
  color: #666;
  margin: 0;
}

.link-button {
  background: none;
  border: none;
  color: #667eea;
  cursor: pointer;
  text-decoration: underline;
  font-size: inherit;
}

.link-button:hover {
  color: #764ba2;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: #333;
}

.form-group input,
.form-group textarea {
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
  font-family: inherit;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-top: 0.5rem;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  cursor: pointer;
  font-size: 0.9rem;
  color: #555;
}

.checkbox-label input[type="checkbox"] {
  width: auto;
  margin: 0;
}

.submit-btn {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 1rem;
}

@media (max-width: 768px) {
  .modal-content {
    padding: 1.5rem;
    margin: 1rem;
  }
  
  .modal-header h2 {
    font-size: 2rem;
  }
  
  .join-options {
    grid-template-columns: 1fr;
  }
  
  .form-row {
    grid-template-columns: 1fr;
  }
  
  .join-card {
    padding: 1.5rem;
  }
  
  .card-icon {
    font-size: 3rem;
  }
}
</style>