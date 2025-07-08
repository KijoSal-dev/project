<template>
  <div id="app">
    <!-- Show main website if no portal is active -->
    <template v-if="!activePortal">
      <Header />
      <main>
        <HeroSection />
        <ProblemSection />
        <FeaturesSection />
        <LearningPlatform @show-portal="showPortal" />
        <CallToAction />
      </main>
      <Footer />
    </template>

    <!-- Show Educator Portal -->
    <EducatorPortal 
      v-if="activePortal === 'educator' && authStore.userProfile.value"
      :user="authStore.userProfile.value"
      @logout="handleLogout"
      @back-to-main="backToMain"
    />

    <!-- Show Student Portal -->
    <StudentPortal 
      v-if="activePortal === 'student' && authStore.userProfile.value"
      :user="authStore.userProfile.value"
      @logout="handleLogout"
      @back-to-main="backToMain"
    />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useAuthStore } from './stores/authStore'
import Header from './components/Header.vue'
import HeroSection from './components/HeroSection.vue'
import ProblemSection from './components/ProblemSection.vue'
import FeaturesSection from './components/FeaturesSection.vue'
import LearningPlatform from './components/LearningPlatform.vue'
import CallToAction from './components/CallToAction.vue'
import Footer from './components/Footer.vue'
import EducatorPortal from './components/EducatorPortal.vue'
import StudentPortal from './components/StudentPortal.vue'

const authStore = useAuthStore()
const activePortal = ref<'educator' | 'student' | null>(null)

const showPortal = (type: 'educator' | 'student') => {
  activePortal.value = type
}

const handleLogout = async () => {
  await authStore.logout()
  activePortal.value = null
}

const backToMain = () => {
  activePortal.value = null
}

onMounted(() => {
  // Check if user is already authenticated and redirect to appropriate portal
  if (authStore.isAuthenticated.value && authStore.userProfile.value) {
    const userRole = authStore.userProfile.value.role
    if (userRole === 'educator' || userRole === 'specialist') {
      activePortal.value = 'educator'
    } else if (userRole === 'student') {
      activePortal.value = 'student'
    }
  }
})
</script>

<style scoped>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}
</style>