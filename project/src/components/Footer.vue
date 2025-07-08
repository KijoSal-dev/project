<template>
  <footer id="contact" class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h3>AI Tutor Kenya</h3>
          <p>Transforming special needs education through innovative AI technology.</p>
          <div class="social-links">
            <a href="#" class="social-link">📧</a>
            <a href="#" class="social-link">📱</a>
            <a href="#" class="social-link">🌐</a>
          </div>
        </div>
        
        <div class="footer-section">
          <h4>Platform</h4>
          <ul>
            <li><a href="#features">Features</a></li>
            <li><a href="#platform">Learning Portal</a></li>
            <li><a href="#contribute">Educator Portal</a></li>
            <li><a href="#">API Documentation</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Community</h4>
          <ul>
            <li><a href="#contribute">Join Us</a></li>
            <li><a href="#">Developer Community</a></li>
            <li><a href="#">Educational Resources</a></li>
            <li><a href="#">Success Stories</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Support</h4>
          <ul>
            <li><a href="#">Help Center</a></li>
            <li><a href="#">Training Materials</a></li>
            <li><a href="#">Technical Support</a></li>
            <li><a href="#">Accessibility Guide</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4>Contact</h4>
          <div class="contact-info">
            <p>📧 info@aitutor.ke</p>
            <p>📱 +254 700 123 456</p>
            <p>🏢 Nairobi, Kenya</p>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <div class="footer-bottom-content">
          <p>&copy; 2024 AI Tutor Kenya. All rights reserved.</p>
          <div class="footer-links">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Accessibility</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
</script>

<style scoped>
.footer {
  background: #1a1a1a;
  color: white;
  padding: 4rem 0 2rem;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 3rem;
  margin-bottom: 3rem;
}

.footer-section h3 {
  color: #ff6b6b;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.footer-section h4 {
  color: white;
  font-size: 1.25rem;
  margin-bottom: 1rem;
}

.footer-section p {
  color: #ccc;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.footer-section ul {
  list-style: none;
  padding: 0;
}

.footer-section li {
  margin-bottom: 0.5rem;
}

.footer-section a {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-section a:hover {
  color: #ff6b6b;
}

.social-links {
  display: flex;
  gap: 1rem;
}

.social-link {
  font-size: 1.5rem;
  transition: transform 0.3s ease;
}

.social-link:hover {
  transform: scale(1.2);
}

.contact-info p {
  margin-bottom: 0.5rem;
}

.footer-bottom {
  border-top: 1px solid #333;
  padding-top: 2rem;
}

.footer-bottom-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

.footer-bottom p {
  color: #ccc;
  margin: 0;
}

.footer-links {
  display: flex;
  gap: 2rem;
}

.footer-links a {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-links a:hover {
  color: #ff6b6b;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  
  .footer-bottom-content {
    flex-direction: column;
    text-align: center;
  }
  
  .footer-links {
    justify-content: center;
  }
}
</style>