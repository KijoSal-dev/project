<template>
  <div class="portal-container">
    <div class="portal-header">
      <div class="header-content">
        <h1>Welcome, {{ user.name }}! 🌟</h1>
        <p>Your personalized learning journey continues</p>
      </div>
      <div class="header-actions">
        <div class="streak-counter">
          <span class="streak-icon">🔥</span>
          <span class="streak-text">{{ streakDays }} day streak!</span>
        </div>
        <button @click="$emit('back-to-main')" class="back-btn">← Back to Main</button>
        <button @click="logout" class="logout-btn">Sign Out</button>
      </div>
    </div>

    <div class="portal-nav">
      <button 
        v-for="tab in tabs" 
        :key="tab.id"
        @click="activeTab = tab.id"
        :class="['nav-tab', { active: activeTab === tab.id }]"
      >
        <span class="tab-icon">{{ tab.icon }}</span>
        {{ tab.label }}
      </button>
    </div>

    <div class="portal-content">
      <!-- Learning Dashboard -->
      <div v-if="activeTab === 'dashboard'" class="tab-content">
        <div class="welcome-section">
          <div class="progress-overview">
            <h2>Your Learning Progress</h2>
            <div class="progress-stats">
              <div class="progress-stat">
                <div class="stat-circle" :style="`--progress: ${overallProgress}%`">
                  <span class="stat-value">{{ overallProgress }}%</span>
                </div>
                <p>Overall Progress</p>
              </div>
              <div class="progress-stat">
                <div class="stat-circle" :style="`--progress: ${(completedLessons / totalLessons) * 100}%`">
                  <span class="stat-value">{{ completedLessons }}</span>
                </div>
                <p>Lessons Completed</p>
              </div>
              <div class="progress-stat">
                <div class="stat-circle" :style="`--progress: ${(pointsEarned / 50) * 100}%`">
                  <span class="stat-value">{{ pointsEarned }}</span>
                </div>
                <p>Points Earned</p>
              </div>
            </div>
          </div>

          <div class="daily-goals">
            <h3>Today's Goals</h3>
            <div class="goal-list">
              <div v-for="goal in dailyGoals" :key="goal.id" :class="['goal-item', { completed: goal.completed }]">
                <span class="goal-icon">{{ goal.completed ? '✅' : '⭕' }}</span>
                <span class="goal-text">{{ goal.text }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="learning-sections">
          <div class="section">
            <h3>Continue Learning</h3>
            <div class="lesson-cards">
              <div v-for="lesson in currentLessons" :key="lesson.id" class="lesson-card">
                <div class="lesson-image">{{ lesson.icon }}</div>
                <div class="lesson-content">
                  <h4>{{ lesson.title }}</h4>
                  <p>{{ lesson.description }}</p>
                  <div class="lesson-progress">
                    <div class="progress-bar">
                      <div class="progress-fill" :style="`width: ${lesson.progress}%`"></div>
                    </div>
                    <span class="progress-text">{{ lesson.progress }}% complete</span>
                  </div>
                </div>
                <button class="btn btn-primary" @click="startLesson(lesson.id)">Continue</button>
              </div>
            </div>
          </div>

          <div class="section">
            <h3>Achievements</h3>
            <div class="achievement-grid">
              <div v-for="achievement in achievements" :key="achievement.id" :class="['achievement-badge', { earned: achievement.earned }]">
                <div class="badge-icon">{{ achievement.icon }}</div>
                <p>{{ achievement.name }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Learning Activities -->
      <div v-if="activeTab === 'activities'" class="tab-content">
        <div class="content-header">
          <h2>Learning Activities</h2>
          <div class="activity-filters">
            <button v-for="filter in activityFilters" :key="filter" 
                    :class="['filter-btn', { active: selectedFilter === filter }]"
                    @click="selectedFilter = filter">
              {{ filter }}
            </button>
          </div>
        </div>

        <div class="activity-grid">
          <div v-for="activity in filteredActivities" :key="activity.id" class="activity-card">
            <div class="activity-header">
              <div class="activity-icon">{{ activity.icon }}</div>
              <div :class="['difficulty-badge', activity.difficulty]">{{ activity.difficulty }}</div>
            </div>
            <h3>{{ activity.title }}</h3>
            <p>{{ activity.description }}</p>
            <div class="activity-meta">
              <span class="duration">⏱️ {{ activity.duration }} min</span>
              <span class="points">⭐ {{ activity.points }} points</span>
            </div>
            <button class="btn btn-primary" @click="startActivity(activity.id)">Start Activity</button>
          </div>
        </div>
      </div>

      <!-- Progress Tracking -->
      <div v-if="activeTab === 'progress'" class="tab-content">
        <div class="content-header">
          <h2>My Progress</h2>
          <div class="time-filter">
            <button v-for="period in timePeriods" :key="period"
                    :class="['time-btn', { active: selectedPeriod === period }]"
                    @click="selectedPeriod = period">
              {{ period }}
            </button>
          </div>
        </div>

        <div class="progress-dashboard">
          <div class="progress-chart-section">
            <h3>Learning Progress</h3>
            <div class="subject-progress">
              <div v-for="subject in subjectProgress" :key="subject.name" class="subject-item">
                <div class="subject-info">
                  <span class="subject-icon">{{ subject.icon }}</span>
                  <span class="subject-name">{{ subject.name }}</span>
                </div>
                <div class="progress-bar">
                  <div class="progress-fill" :style="`width: ${subject.progress}%`"></div>
                </div>
                <span class="progress-percentage">{{ subject.progress }}%</span>
              </div>
            </div>
          </div>

          <div class="milestones-section">
            <h3>Recent Milestones</h3>
            <div class="milestone-list">
              <div v-for="milestone in recentMilestones" :key="milestone.id" class="milestone-item">
                <div class="milestone-icon">{{ milestone.icon }}</div>
                <div class="milestone-content">
                  <h4>{{ milestone.title }}</h4>
                  <p>{{ milestone.description }}</p>
                  <span class="milestone-date">{{ milestone.date }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Support & Help -->
      <div v-if="activeTab === 'support'" class="tab-content">
        <div class="content-header">
          <h2>Support & Help</h2>
        </div>

        <div class="support-sections">
          <div class="help-categories">
            <div v-for="category in helpCategories" :key="category.id" class="help-card">
              <div class="help-icon">{{ category.icon }}</div>
              <h3>{{ category.title }}</h3>
              <p>{{ category.description }}</p>
              <button class="btn btn-secondary" @click="openHelp(category.id)">{{ category.buttonText }}</button>
            </div>
          </div>

          <div class="quick-actions">
            <h3>Quick Actions</h3>
            <div class="action-list">
              <button v-for="action in quickActions" :key="action.id" class="action-item" @click="performAction(action.id)">
                <span class="action-icon">{{ action.icon }}</span>
                <span class="action-text">{{ action.text }}</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

interface Props {
  user: {
    name: string
    email: string
    role: string
  }
}

interface Emits {
  (e: 'logout'): void
  (e: 'back-to-main'): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const activeTab = ref('dashboard')
const selectedFilter = ref('All')
const selectedPeriod = ref('This Week')

// Dashboard data
const streakDays = ref(7)
const overallProgress = ref(75)
const completedLessons = ref(12)
const totalLessons = ref(20)
const pointsEarned = ref(45)

const tabs = [
  { id: 'dashboard', label: 'Dashboard', icon: '🏠' },
  { id: 'activities', label: 'Activities', icon: '🎮' },
  { id: 'progress', label: 'My Progress', icon: '📈' },
  { id: 'support', label: 'Help', icon: '💬' }
]

const dailyGoals = ref([
  { id: 1, text: 'Complete Math Practice', completed: true },
  { id: 2, text: 'Read for 15 minutes', completed: false },
  { id: 3, text: 'Practice social skills', completed: false }
])

const currentLessons = ref([
  {
    id: 1,
    icon: '📚',
    title: 'Reading Adventures',
    description: 'Interactive stories with comprehension activities',
    progress: 60
  },
  {
    id: 2,
    icon: '🔢',
    title: 'Number Fun',
    description: 'Visual math games and counting exercises',
    progress: 30
  },
  {
    id: 3,
    icon: '🎨',
    title: 'Creative Expression',
    description: 'Art and creativity activities for self-expression',
    progress: 85
  }
])

const achievements = ref([
  { id: 1, icon: '🏆', name: 'First Lesson', earned: true },
  { id: 2, icon: '📖', name: 'Reading Star', earned: true },
  { id: 3, icon: '🔥', name: 'Week Streak', earned: true },
  { id: 4, icon: '🎯', name: 'Goal Getter', earned: false },
  { id: 5, icon: '🌟', name: 'Super Learner', earned: false },
  { id: 6, icon: '🎨', name: 'Creative Genius', earned: false }
])

const activityFilters = ref(['All', 'Math', 'Reading', 'Social', 'Creative'])

const activities = ref([
  {
    id: 1,
    icon: '🎯',
    title: 'Shape Sorting',
    description: 'Learn about different shapes through interactive sorting games',
    difficulty: 'easy',
    duration: 10,
    points: 5,
    category: 'Math'
  },
  {
    id: 2,
    icon: '📚',
    title: 'Story Builder',
    description: 'Create your own stories with pictures and simple words',
    difficulty: 'medium',
    duration: 15,
    points: 8,
    category: 'Reading'
  },
  {
    id: 3,
    icon: '🎵',
    title: 'Music Patterns',
    description: 'Learn patterns and sequences through musical activities',
    difficulty: 'easy',
    duration: 12,
    points: 6,
    category: 'Creative'
  },
  {
    id: 4,
    icon: '👥',
    title: 'Social Scenarios',
    description: 'Practice social interactions in safe, guided environments',
    difficulty: 'medium',
    duration: 20,
    points: 10,
    category: 'Social'
  },
  {
    id: 5,
    icon: '🧮',
    title: 'Number Bonds',
    description: 'Understanding relationships between numbers through visual aids',
    difficulty: 'medium',
    duration: 18,
    points: 12,
    category: 'Math'
  },
  {
    id: 6,
    icon: '🎭',
    title: 'Emotion Theater',
    description: 'Learn to recognize and express emotions through role-play',
    difficulty: 'easy',
    duration: 14,
    points: 7,
    category: 'Social'
  }
])

const timePeriods = ref(['This Week', 'This Month', 'All Time'])

const subjectProgress = ref([
  { name: 'Reading', icon: '📚', progress: 75 },
  { name: 'Math', icon: '🔢', progress: 60 },
  { name: 'Social Skills', icon: '👥', progress: 45 },
  { name: 'Creative Arts', icon: '🎨', progress: 80 }
])

const recentMilestones = ref([
  {
    id: 1,
    icon: '🎉',
    title: 'Completed Level 3 Reading',
    description: 'Great job on finishing all reading exercises!',
    date: '2 days ago'
  },
  {
    id: 2,
    icon: '⭐',
    title: 'Perfect Math Score',
    description: 'You got all addition problems correct!',
    date: '5 days ago'
  },
  {
    id: 3,
    icon: '🏆',
    title: 'Social Skills Champion',
    description: 'Excellent progress in communication activities',
    date: '1 week ago'
  }
])

const helpCategories = ref([
  {
    id: 'learning',
    icon: '🎯',
    title: 'Learning Help',
    description: 'Get assistance with activities and lessons',
    buttonText: 'Get Help'
  },
  {
    id: 'technical',
    icon: '⚙️',
    title: 'Technical Support',
    description: 'Having trouble with the app? We\'re here to help',
    buttonText: 'Contact Support'
  },
  {
    id: 'family',
    icon: '👨‍👩‍👧‍👦',
    title: 'Parent/Guardian',
    description: 'Resources and updates for families',
    buttonText: 'Family Portal'
  }
])

const quickActions = ref([
  { id: 'voice', icon: '🔊', text: 'Turn on voice assistance' },
  { id: 'theme', icon: '🎨', text: 'Change theme colors' },
  { id: 'text', icon: '📝', text: 'Adjust text size' },
  { id: 'reminders', icon: '⏰', text: 'Set learning reminders' }
])

const filteredActivities = computed(() => {
  if (selectedFilter.value === 'All') {
    return activities.value
  }
  return activities.value.filter(activity => activity.category === selectedFilter.value)
})

const startLesson = (lessonId: number) => {
  console.log('Starting lesson:', lessonId)
  // Here you would navigate to the lesson or open a lesson modal
}

const startActivity = (activityId: number) => {
  console.log('Starting activity:', activityId)
  // Here you would navigate to the activity or open an activity modal
}

const openHelp = (categoryId: string) => {
  console.log('Opening help for:', categoryId)
  // Here you would open help modal or navigate to help section
}

const performAction = (actionId: string) => {
  console.log('Performing action:', actionId)
  // Here you would perform the specific action
}

const logout = () => {
  emit('logout')
}
</script>

<style scoped>
.portal-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.portal-header {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  color: white;
  padding: 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header-content h1 {
  margin: 0 0 0.5rem 0;
  font-size: 2rem;
}

.header-content p {
  margin: 0;
  opacity: 0.9;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.streak-counter {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.75rem 1rem;
  border-radius: 25px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.streak-icon {
  font-size: 1.2rem;
}

.streak-text {
  font-weight: 600;
  font-size: 0.9rem;
}

.back-btn,
.logout-btn {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.back-btn:hover,
.logout-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.portal-nav {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 0 2rem;
  display: flex;
  gap: 1rem;
  overflow-x: auto;
}

.nav-tab {
  background: none;
  border: none;
  padding: 1rem 1.5rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #666;
  border-bottom: 3px solid transparent;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.nav-tab.active {
  color: #f5576c;
  border-bottom-color: #f5576c;
}

.nav-tab:hover {
  color: #f5576c;
}

.tab-icon {
  font-size: 1.2rem;
}

.portal-content {
  padding: 2rem;
  min-height: calc(100vh - 200px);
}

.tab-content {
  max-width: 1200px;
  margin: 0 auto;
}

.welcome-section {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}

.progress-overview {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.progress-overview h2 {
  margin: 0 0 2rem 0;
  color: #333;
}

.progress-stats {
  display: flex;
  justify-content: space-around;
  gap: 1rem;
}

.progress-stat {
  text-align: center;
}

.stat-circle {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: conic-gradient(#f5576c 0deg, #f5576c calc(var(--progress) * 3.6deg), #e0e0e0 calc(var(--progress) * 3.6deg));
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 1rem auto;
  position: relative;
}

.stat-circle::before {
  content: '';
  width: 60px;
  height: 60px;
  background: white;
  border-radius: 50%;
  position: absolute;
}

.stat-value {
  position: relative;
  z-index: 1;
  font-weight: 700;
  color: #333;
}

.progress-stat p {
  margin: 0;
  font-size: 0.9rem;
  color: #666;
}

.daily-goals {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.daily-goals h3 {
  margin: 0 0 1.5rem 0;
  color: #333;
}

.goal-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.goal-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 15px;
  transition: all 0.3s ease;
}

.goal-item.completed {
  background: #d4edda;
}

.goal-icon {
  font-size: 1.5rem;
}

.goal-text {
  font-weight: 500;
  color: #333;
}

.learning-sections {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.section h3 {
  margin: 0 0 1.5rem 0;
  color: #333;
}

.lesson-cards {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.lesson-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.5rem;
  background: white;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.lesson-card:hover {
  transform: translateY(-2px);
}

.lesson-image {
  font-size: 3rem;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8f9fa;
  border-radius: 15px;
  flex-shrink: 0;
}

.lesson-content {
  flex: 1;
}

.lesson-content h4 {
  margin: 0 0 0.5rem 0;
  color: #333;
}

.lesson-content p {
  margin: 0 0 1rem 0;
  color: #666;
  font-size: 0.9rem;
}

.lesson-progress {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.progress-bar {
  flex: 1;
  height: 8px;
  background: #e0e0e0;
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.8rem;
  color: #666;
  white-space: nowrap;
}

.achievement-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 1rem;
}

.achievement-badge {
  text-align: center;
  padding: 1rem;
  border-radius: 15px;
  background: #f8f9fa;
  opacity: 0.5;
  transition: all 0.3s ease;
}

.achievement-badge.earned {
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  color: white;
  opacity: 1;
  transform: scale(1.05);
}

.badge-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.achievement-badge p {
  margin: 0;
  font-size: 0.8rem;
  font-weight: 600;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.content-header h2 {
  margin: 0;
  color: white;
}

.activity-filters,
.time-filter {
  display: flex;
  gap: 0.5rem;
}

.filter-btn,
.time-btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.2);
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
}

.filter-btn.active,
.time-btn.active {
  background: rgba(255, 255, 255, 0.9);
  color: #f5576c;
}

.activity-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.activity-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.activity-card:hover {
  transform: translateY(-5px);
}

.activity-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.activity-icon {
  font-size: 2.5rem;
}

.difficulty-badge {
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: capitalize;
}

.difficulty-badge.easy {
  background: #d4edda;
  color: #155724;
}

.difficulty-badge.medium {
  background: #fff3cd;
  color: #856404;
}

.difficulty-badge.hard {
  background: #f8d7da;
  color: #721c24;
}

.activity-card h3 {
  margin: 0 0 1rem 0;
  color: #333;
}

.activity-card p {
  margin: 0 0 1.5rem 0;
  color: #666;
  line-height: 1.5;
}

.activity-meta {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  color: #666;
}

.progress-dashboard {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.progress-chart-section,
.milestones-section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.subject-progress {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.subject-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-width: 120px;
}

.subject-icon {
  font-size: 1.5rem;
}

.subject-name {
  font-weight: 600;
  color: #333;
}

.progress-percentage {
  font-weight: 600;
  color: #f5576c;
  min-width: 40px;
  text-align: right;
}

.milestone-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.milestone-item {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 15px;
}

.milestone-icon {
  font-size: 2rem;
  flex-shrink: 0;
}

.milestone-content h4 {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 1rem;
}

.milestone-content p {
  margin: 0 0 0.5rem 0;
  color: #666;
  font-size: 0.9rem;
}

.milestone-date {
  font-size: 0.8rem;
  color: #999;
}

.support-sections {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.help-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.help-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  text-align: center;
  transition: transform 0.3s ease;
}

.help-card:hover {
  transform: translateY(-5px);
}

.help-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.help-card h3 {
  margin: 0 0 1rem 0;
  color: #333;
}

.help-card p {
  margin: 0 0 1.5rem 0;
  color: #666;
  line-height: 1.5;
}

.quick-actions {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.quick-actions h3 {
  margin: 0 0 1.5rem 0;
  color: #333;
}

.action-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.action-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border: none;
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: left;
  width: 100%;
}

.action-item:hover {
  background: #e9ecef;
  transform: translateX(5px);
}

.action-icon {
  font-size: 1.5rem;
}

.action-text {
  font-weight: 500;
  color: #333;
}

@media (max-width: 768px) {
  .portal-header {
    flex-direction: column;
    gap: 1rem;
    text-align: center;
  }
  
  .header-actions {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .portal-nav {
    padding: 0 1rem;
  }
  
  .portal-content {
    padding: 1rem;
  }
  
  .welcome-section,
  .learning-sections,
  .progress-dashboard,
  .support-sections {
    grid-template-columns: 1fr;
  }
  
  .progress-stats {
    flex-direction: column;
    align-items: center;
    gap: 2rem;
  }
  
  .content-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .activity-grid {
    grid-template-columns: 1fr;
  }
  
  .help-categories {
    grid-template-columns: 1fr;
  }
}
</style>