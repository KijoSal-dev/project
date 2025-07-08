<template>
  <section id="home" class="hero">
    <div class="hero-container">
      <div class="hero-content">
        <h1 class="hero-title">
          Transforming Special Needs Education in Kenya
        </h1>
        <p class="hero-subtitle">
          AI-powered personalized learning platform designed specifically for students with special needs, 
          empowering educators and creating inclusive educational environments across Kenya.
        </p>
        <div class="hero-buttons">
          <button class="btn btn-primary">Start Learning</button>
          <button class="btn btn-secondary">For Educators</button>
        </div>
        <div class="hero-stats">
          <div class="stat">
            <span class="stat-number">10,000+</span>
            <span class="stat-label">Students Supported</span>
          </div>
          <div class="stat">
            <span class="stat-number">500+</span>
            <span class="stat-label">Educators Trained</span>
          </div>
          <div class="stat">
            <span class="stat-number">47</span>
            <span class="stat-label">Counties Reached</span>
          </div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-graphic">
          <div class="floating-card card-1">
            <div class="card-icon">🎓</div>
            <div class="card-text">Personalized Learning</div>
          </div>
          <div class="floating-card card-2">
            <div class="card-icon">🤖</div>
            <div class="card-text">AI-Powered</div>
          </div>
          <div class="floating-card card-3">
            <div class="card-icon">♿</div>
            <div class="card-text">Accessible Design</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 8rem 0 4rem;
  margin-top: 80px;
  min-height: 80vh;
  display: flex;
  align-items: center;
}

.hero-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  line-height: 1.2;
  margin-bottom: 1.5rem;
}

.hero-subtitle {
  font-size: 1.25rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  margin-bottom: 3rem;
}

.btn {
  padding: 1rem 2rem;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-block;
}

.btn-primary {
  background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
}

.btn-secondary {
  background: transparent;
  color: white;
  border: 2px solid white;
}

.btn-secondary:hover {
  background: white;
  color: #667eea;
}

.hero-stats {
  display: flex;
  gap: 2rem;
}

.stat {
  text-align: center;
}

.stat-number {
  display: block;
  font-size: 2rem;
  font-weight: 700;
  color: #ff6b6b;
}

.stat-label {
  font-size: 0.875rem;
  opacity: 0.8;
}

.hero-visual {
  position: relative;
  height: 400px;
}

.hero-graphic {
  position: relative;
  width: 100%;
  height: 100%;
}

.floating-card {
  position: absolute;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 1.5rem;
  text-align: center;
  animation: float 3s ease-in-out infinite;
}

.card-1 {
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.card-2 {
  top: 50%;
  right: 10%;
  animation-delay: 1s;
}

.card-3 {
  bottom: 20%;
  left: 20%;
  animation-delay: 2s;
}

.card-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.card-text {
  font-size: 0.875rem;
  font-weight: 600;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@media (max-width: 768px) {
  .hero-container {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1.1rem;
  }

  .hero-buttons {
    justify-content: center;
  }

  .hero-stats {
    justify-content: center;
  }

  .hero-visual {
    height: 300px;
  }
}
</style>