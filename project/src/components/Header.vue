<template>
  <header class="header">
    <nav class="nav">
      <div class="nav-container">
        <div class="logo">
          <h1>AI Tutor Kenya</h1>
          <span class="tagline">Empowering Special Needs Education</span>
        </div>
        
        <ul class="nav-menu" :class="{ 'active': menuOpen }">
          <li><a href="#home" @click="closeMenu">Home</a></li>
          <li><a href="#features" @click="closeMenu">Features</a></li>
          <li><a href="#platform" @click="closeMenu">Platform</a></li>
          <li><a href="#contribute" @click="closeMenu">Contribute</a></li>
          <li><a href="#contact" @click="closeMenu">Contact</a></li>
        </ul>
        
        <button class="menu-toggle" @click="toggleMenu" :aria-expanded="menuOpen">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </nav>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}

const closeMenu = () => {
  menuOpen.value = false
}
</script>

<style scoped>
.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 1rem 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: 700;
}

.tagline {
  font-size: 0.875rem;
  opacity: 0.9;
  display: block;
  margin-top: 0.25rem;
}

.nav-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 2rem;
}

.nav-menu a {
  color: white;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.3s ease;
}

.nav-menu a:hover {
  opacity: 0.8;
}

.menu-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.menu-toggle span {
  width: 25px;
  height: 3px;
  background: white;
  margin: 3px 0;
  transition: 0.3s;
}

@media (max-width: 768px) {
  .nav-menu {
    position: fixed;
    top: 100%;
    left: 0;
    width: 100%;
    height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 3rem;
    transform: translateY(-100%);
    transition: transform 0.3s ease;
  }

  .nav-menu.active {
    transform: translateY(0);
  }

  .menu-toggle {
    display: flex;
  }

  .nav-menu a {
    font-size: 1.5rem;
  }
}
</style>