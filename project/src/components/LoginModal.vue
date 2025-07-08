<template>
  <div v-if="isOpen" class="modal-overlay" @click="closeModal">
    <div class="modal-content" @click.stop>
      <button class="modal-close" @click="closeModal">&times;</button>
      
      <div class="modal-header">
        <h2>{{ modalTitle }}</h2>
        <p>{{ modalSubtitle }}</p>
      </div>
      
      <div class="auth-tabs">
        <button 
          class="tab-button" 
          :class="{ active: authMode === 'login' }"
          @click="authMode = 'login'"
        >
          Sign In
        </button>
        <button 
          class="tab-button" 
          :class="{ active: authMode === 'register' }"
          @click="authMode = 'register'"
        >
          Create Account
        </button>
      </div>
      
      <form @submit.prevent="handleSubmit" class="auth-form">
        <div v-if="authMode === 'register'" class="form-group">
          <label for="fullName">Full Name</label>
          <input 
            type="text" 
            id="fullName" 
            v-model="form.fullName" 
            required 
            placeholder="Enter your full name"
          >
        </div>
        
        <div class="form-group">
          <label for="email">Email Address</label>
          <input 
            type="email" 
            id="email" 
            v-model="form.email" 
            required 
            placeholder="Enter your email"
          >
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <input 
            type="password" 
            id="password" 
            v-model="form.password" 
            required 
            placeholder="Enter your password"
            :minlength="authMode === 'register' ? 6 : undefined"
          >
        </div>
        
        <div v-if="authMode === 'register'" class="form-group">
          <label for="role">I am a:</label>
          <select id="role" v-model="form.role" required>
            <option value="">Select your role</option>
            <option value="student">Student/Learner</option>
            <option value="educator">Educator/Teacher</option>
            <option value="parent">Parent/Guardian</option>
            <option value="specialist">Special Needs Specialist</option>
          </select>
        </div>
        
        <div v-if="authMode === 'register'" class="form-group">
          <label class="checkbox-label">
            <input type="checkbox" v-model="form.agreeTerms" required>
            <span class="checkmark"></span>
            I agree to the <a href="#" class="link">Terms of Service</a> and <a href="#" class="link">Privacy Policy</a>
          </label>
        </div>

        <div v-if="authStore.error.value" class="error-message">
          {{ authStore.error.value }}
        </div>
        
        <button type="submit" class="btn btn-primary auth-submit" :disabled="authStore.isLoading.value">
          {{ authStore.isLoading.value ? 'Please wait...' : (authMode === 'login' ? 'Sign In' : 'Create Account') }}
        </button>
      </form>
      
      <div class="auth-footer">
        <p v-if="authMode === 'login'">
          Don't have an account? 
          <button @click="authMode = 'register'" class="link-button">Sign up here</button>
        </p>
        <p v-else>
          Already have an account? 
          <button @click="authMode = 'login'" class="link-button">Sign in here</button>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useAuthStore } from '../stores/authStore'

interface Props {
  isOpen: boolean
  portalType: 'educator' | 'student'
}

interface Emits {
  (e: 'close'): void
  (e: 'login-success', type: 'educator' | 'student'): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const authStore = useAuthStore()
const authMode = ref<'login' | 'register'>('login')

const form = ref({
  fullName: '',
  email: '',
  password: '',
  role: '',
  agreeTerms: false
})

const modalTitle = computed(() => {
  if (props.portalType === 'educator') {
    return authMode.value === 'login' ? 'Educator Portal Access' : 'Join as Educator'
  }
  return authMode.value === 'login' ? 'Student Portal Access' : 'Start Learning Journey'
})

const modalSubtitle = computed(() => {
  if (props.portalType === 'educator') {
    return 'Access your teaching dashboard and resources'
  }
  return 'Begin your personalized learning experience'
})

const closeModal = () => {
  emit('close')
  resetForm()
  authStore.clearError()
}

const resetForm = () => {
  form.value = {
    fullName: '',
    email: '',
    password: '',
    role: '',
    agreeTerms: false
  }
  authMode.value = 'login'
}

const handleSubmit = async () => {
  authStore.clearError()
  
  try {
    if (authMode.value === 'login') {
      await authStore.signIn(form.value.email, form.value.password)
    } else {
      const role = form.value.role || props.portalType
      await authStore.signUp(form.value.email, form.value.password, form.value.fullName, role)
    }
    
    // Emit success with portal type
    emit('login-success', props.portalType)
    resetForm()
  } catch (error) {
    // Error is handled by the auth store
    console.error('Authentication error:', error)
  }
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
  max-width: 500px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
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
}

.modal-close:hover {
  color: #333;
}

.modal-header {
  text-align: center;
  margin-bottom: 2rem;
}

.modal-header h2 {
  color: #333;
  margin-bottom: 0.5rem;
}

.modal-header p {
  color: #666;
  margin: 0;
}

.auth-tabs {
  display: flex;
  margin-bottom: 2rem;
  border-bottom: 1px solid #e0e0e0;
}

.tab-button {
  flex: 1;
  padding: 1rem;
  background: none;
  border: none;
  cursor: pointer;
  font-weight: 600;
  color: #666;
  border-bottom: 2px solid transparent;
  transition: all 0.3s ease;
}

.tab-button.active {
  color: #667eea;
  border-bottom-color: #667eea;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
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
.form-group select {
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 1rem;
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.checkbox-label {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  cursor: pointer;
  font-size: 0.9rem;
  line-height: 1.4;
}

.checkbox-label input[type="checkbox"] {
  width: auto;
  margin: 0;
}

.link {
  color: #667eea;
  text-decoration: none;
}

.link:hover {
  text-decoration: underline;
}

.error-message {
  background: #fee;
  color: #c33;
  padding: 1rem;
  border-radius: 8px;
  font-size: 0.9rem;
  border: 1px solid #fcc;
}

.auth-submit {
  width: 100%;
  padding: 1rem;
  font-size: 1.1rem;
  margin-top: 1rem;
}

.auth-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.auth-footer {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #e0e0e0;
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

@media (max-width: 768px) {
  .modal-content {
    padding: 1.5rem;
    margin: 1rem;
  }
  
  .modal-header h2 {
    font-size: 1.5rem;
  }
}
</style>