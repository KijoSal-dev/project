<template>
  <section class="problem-section">
    <div class="container">
      <div class="content-grid">
        <div class="problem-content">
          <h2>The Challenge in Kenya</h2>
          <p class="lead">
            Over 1.3 million Kenyan children have special needs, yet only 10% have access to specialized education. 
            Traditional teaching methods often fail to address diverse learning requirements.
          </p>
          
          <div class="problem-stats">
            <div class="problem-stat">
              <span class="stat-number">1.3M+</span>
              <span class="stat-text">Children with special needs</span>
            </div>
            <div class="problem-stat">
              <span class="stat-number">10%</span>
              <span class="stat-text">Have access to specialized education</span>
            </div>
            <div class="problem-stat">
              <span class="stat-number">47</span>
              <span class="stat-text">Counties lacking resources</span>
            </div>
          </div>
        </div>
        
        <div class="solution-content">
          <h2>Our AI-Powered Solution</h2>
          <p class="lead">
            We're bridging this gap with cutting-edge AI technology that adapts to each learner's unique needs, 
            providing personalized support for students, teachers, and families.
          </p>
          
          <div class="solution-points">
            <div class="solution-point">
              <div class="point-icon">🎯</div>
              <div class="point-text">
                <h3>Personalized Learning</h3>
                <p>AI adapts to individual learning styles and paces</p>
              </div>
            </div>
            <div class="solution-point">
              <div class="point-icon">🌍</div>
              <div class="point-text">
                <h3>Nationwide Access</h3>
                <p>Cloud-based platform reaching every corner of Kenya</p>
              </div>
            </div>
            <div class="solution-point">
              <div class="point-icon">👥</div>
              <div class="point-text">
                <h3>Community Support</h3>
                <p>Connecting educators, families, and specialists</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
</script>

<style scoped>
.problem-section {
  padding: 6rem 0;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.problem-content,
.solution-content {
  padding: 2rem;
}

.problem-content {
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.solution-content {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

h2 {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: #333;
}

.solution-content h2 {
  color: white;
}

.lead {
  font-size: 1.25rem;
  line-height: 1.6;
  margin-bottom: 2rem;
  color: #666;
}

.solution-content .lead {
  color: rgba(255, 255, 255, 0.9);
}

.problem-stats {
  display: flex;
  gap: 2rem;
  margin-top: 2rem;
}

.problem-stat {
  text-align: center;
}

.problem-stat .stat-number {
  display: block;
  font-size: 2rem;
  font-weight: 700;
  color: #ff6b6b;
}

.problem-stat .stat-text {
  font-size: 0.875rem;
  color: #666;
  margin-top: 0.5rem;
}

.solution-points {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.solution-point {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
}

.point-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.point-text h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.25rem;
  color: white;
}

.point-text p {
  margin: 0;
  opacity: 0.9;
  line-height: 1.5;
}

@media (max-width: 768px) {
  .content-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .problem-stats {
    flex-direction: column;
    gap: 1rem;
  }

  h2 {
    font-size: 2rem;
  }

  .lead {
    font-size: 1.1rem;
  }
}
</style>