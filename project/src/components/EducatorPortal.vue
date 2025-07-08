<template>
  <div class="portal-container">
    <div class="portal-header">
      <div class="header-content">
        <h1>Welcome back, {{ user.name }}!</h1>
        <p>Educator Dashboard - Empowering Special Needs Education</p>
      </div>
      <div class="header-actions">
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
      <!-- Dashboard Overview -->
      <div v-if="activeTab === 'dashboard'" class="tab-content">
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">👥</div>
            <div class="stat-info">
              <h3>{{ dashboardData.activeStudents }}</h3>
              <p>Active Students</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📚</div>
            <div class="stat-info">
              <h3>{{ dashboardData.lessonsCreated }}</h3>
              <p>Lessons Created</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">📈</div>
            <div class="stat-info">
              <h3>{{ dashboardData.avgProgress }}%</h3>
              <p>Avg. Progress Rate</p>
            </div>
          </div>
          <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <div class="stat-info">
              <h3>{{ dashboardData.satisfaction }}</h3>
              <p>Student Satisfaction</p>
            </div>
          </div>
        </div>

        <div class="dashboard-sections">
          <div class="section">
            <h3>Recent Student Activity</h3>
            <div class="activity-list">
              <div v-for="activity in recentActivities" :key="activity.id" class="activity-item">
                <div class="activity-avatar">{{ activity.avatar }}</div>
                <div class="activity-details">
                  <p><strong>{{ activity.studentName }}</strong> {{ activity.action }}</p>
                  <span class="activity-time">{{ activity.timeAgo }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <h3>Upcoming Tasks</h3>
            <div class="task-list">
              <div v-for="task in upcomingTasks" :key="task.id" class="task-item">
                <input type="checkbox" :id="`task${task.id}`" v-model="task.completed">
                <label :for="`task${task.id}`">{{ task.description }}</label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Lesson Planning -->
      <div v-if="activeTab === 'lessons'" class="tab-content">
        <div class="content-header">
          <h2>Lesson Planning & Management</h2>
          <button class="btn btn-primary" @click="showCreateLessonModal = true">Create New Lesson</button>
        </div>

        <div class="lesson-tools">
          <div class="tool-card" @click="showAIGenerator = true">
            <div class="tool-icon">🎯</div>
            <h3>AI Lesson Generator</h3>
            <p>Create personalized lessons based on student needs and learning objectives</p>
            <button class="btn btn-secondary">Generate Lesson</button>
          </div>
          
          <div class="tool-card" @click="showIEPTracker = true">
            <div class="tool-icon">📝</div>
            <h3>IEP Goal Tracker</h3>
            <p>Align lessons with Individual Education Program goals and track progress</p>
            <button class="btn btn-secondary">Manage IEPs</button>
          </div>
          
          <div class="tool-card" @click="showMaterialsCreator = true">
            <div class="tool-icon">🎨</div>
            <h3>Adaptive Materials</h3>
            <p>Modify existing content for different learning styles and abilities</p>
            <button class="btn btn-secondary">Create Materials</button>
          </div>
        </div>

        <div class="recent-lessons">
          <h3>Recent Lessons</h3>
          <div class="lesson-grid">
            <div v-for="lesson in recentLessons" :key="lesson.id" class="lesson-card">
              <h4>{{ lesson.title }}</h4>
              <p>{{ lesson.description }}</p>
              <div class="lesson-meta">
                <span class="lesson-subject">{{ lesson.subject }}</span>
                <span class="lesson-level">{{ lesson.level }}</span>
              </div>
              <div class="lesson-actions">
                <button class="btn btn-sm">Edit</button>
                <button class="btn btn-sm">Duplicate</button>
                <button class="btn btn-sm">Share</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Student Progress -->
      <div v-if="activeTab === 'progress'" class="tab-content">
        <div class="content-header">
          <h2>Student Progress & Analytics</h2>
          <div class="filter-controls">
            <select class="filter-select" v-model="selectedGroup">
              <option value="all">All Students</option>
              <option value="math">Math Group</option>
              <option value="reading">Reading Group</option>
              <option value="social">Social Skills Group</option>
            </select>
          </div>
        </div>

        <div class="progress-overview">
          <div class="progress-chart">
            <h3>Class Progress Overview</h3>
            <div class="chart-placeholder">
              <div v-for="subject in progressData" :key="subject.name" class="chart-bar" :style="{ height: subject.progress + '%' }">
                <span class="bar-label">{{ subject.name }}</span>
              </div>
            </div>
          </div>

          <div class="student-alerts">
            <h3>Student Alerts</h3>
            <div v-for="alert in studentAlerts" :key="alert.id" :class="['alert-item', alert.type]">
              <span class="alert-icon">{{ alert.icon }}</span>
              <div>
                <p><strong>{{ alert.studentName }}</strong> {{ alert.message }}</p>
                <span class="alert-suggestion">{{ alert.suggestion }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="detailed-progress">
          <h3>Individual Student Progress</h3>
          <div class="student-progress-grid">
            <div v-for="student in studentProgress" :key="student.id" class="student-card">
              <div class="student-header">
                <div class="student-avatar">{{ student.avatar }}</div>
                <div class="student-info">
                  <h4>{{ student.name }}</h4>
                  <p>{{ student.grade }} • {{ student.specialNeeds }}</p>
                </div>
              </div>
              <div class="progress-subjects">
                <div v-for="subject in student.subjects" :key="subject.name" class="subject-progress">
                  <span class="subject-name">{{ subject.name }}</span>
                  <div class="progress-bar">
                    <div class="progress-fill" :style="{ width: subject.progress + '%' }"></div>
                  </div>
                  <span class="progress-text">{{ subject.progress }}%</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Resources -->
      <div v-if="activeTab === 'resources'" class="tab-content">
        <div class="content-header">
          <h2>Teaching Resources & Library</h2>
          <div class="search-bar">
            <input type="text" placeholder="Search resources..." class="search-input" v-model="searchQuery">
            <button class="search-btn">🔍</button>
          </div>
        </div>

        <div class="resource-categories">
          <div v-for="category in resourceCategories" :key="category.id" class="category-card" @click="selectCategory(category.id)">
            <div class="category-icon">{{ category.icon }}</div>
            <h3>{{ category.name }}</h3>
            <p>{{ category.description }}</p>
            <span class="resource-count">{{ category.count }} resources</span>
          </div>
        </div>

        <div v-if="selectedCategory" class="resource-list">
          <h3>{{ getCategoryName(selectedCategory) }} Resources</h3>
          <div class="resources-grid">
            <div v-for="resource in filteredResources" :key="resource.id" class="resource-item">
              <div class="resource-header">
                <div class="resource-type">{{ resource.type }}</div>
                <div class="resource-rating">⭐ {{ resource.rating }}</div>
              </div>
              <h4>{{ resource.title }}</h4>
              <p>{{ resource.description }}</p>
              <div class="resource-tags">
                <span v-for="tag in resource.tags" :key="tag" class="tag">{{ tag }}</span>
              </div>
              <div class="resource-actions">
                <button class="btn btn-sm">Download</button>
                <button class="btn btn-sm">Preview</button>
                <button class="btn btn-sm">Save</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Community -->
      <div v-if="activeTab === 'community'" class="tab-content">
        <div class="content-header">
          <h2>Educator Community</h2>
          <button class="btn btn-primary" @click="showDiscussionModal = true">Start Discussion</button>
        </div>

        <div class="community-sections">
          <div class="discussion-topics">
            <h3>Recent Discussions</h3>
            <div v-for="topic in discussionTopics" :key="topic.id" class="topic-item">
              <div class="topic-avatar">{{ topic.avatar }}</div>
              <div class="topic-content">
                <h4>{{ topic.title }}</h4>
                <p>{{ topic.preview }}</p>
                <div class="topic-meta">
                  <span>{{ topic.replies }} replies</span>
                  <span>{{ topic.timeAgo }}</span>
                  <span class="topic-category">{{ topic.category }}</span>
                </div>
              </div>
            </div>
          </div>

          <div class="community-events">
            <h3>Upcoming Events</h3>
            <div v-for="event in upcomingEvents" :key="event.id" class="event-item">
              <div class="event-date">
                <span class="date-day">{{ event.day }}</span>
                <span class="date-month">{{ event.month }}</span>
              </div>
              <div class="event-details">
                <h4>{{ event.title }}</h4>
                <p>{{ event.description }}</p>
                <span class="event-time">{{ event.time }}</span>
              </div>
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
const selectedGroup = ref('all')
const selectedCategory = ref<string | null>(null)
const searchQuery = ref('')
const showCreateLessonModal = ref(false)
const showAIGenerator = ref(false)
const showIEPTracker = ref(false)
const showMaterialsCreator = ref(false)
const showDiscussionModal = ref(false)

const tabs = [
  { id: 'dashboard', label: 'Dashboard', icon: '📊' },
  { id: 'lessons', label: 'Lesson Planning', icon: '📚' },
  { id: 'progress', label: 'Student Progress', icon: '📈' },
  { id: 'resources', label: 'Resources', icon: '🎯' },
  { id: 'community', label: 'Community', icon: '👥' }
]

const dashboardData = ref({
  activeStudents: 24,
  lessonsCreated: 156,
  avgProgress: 89,
  satisfaction: 4.8
})

const recentActivities = ref([
  {
    id: 1,
    avatar: '👦',
    studentName: 'John M.',
    action: 'completed Math Basics Level 3',
    timeAgo: '2 hours ago'
  },
  {
    id: 2,
    avatar: '👧',
    studentName: 'Sarah K.',
    action: 'needs help with Reading Comprehension',
    timeAgo: '4 hours ago'
  },
  {
    id: 3,
    avatar: '👦',
    studentName: 'David L.',
    action: 'achieved new milestone in Social Skills',
    timeAgo: '1 day ago'
  }
])

const upcomingTasks = ref([
  { id: 1, description: 'Review IEP goals for 5 students', completed: false },
  { id: 2, description: 'Prepare adaptive materials for next week', completed: false },
  { id: 3, description: 'Parent conference with Johnson family', completed: true }
])

const recentLessons = ref([
  {
    id: 1,
    title: 'Basic Math Operations',
    description: 'Visual and tactile approach to addition and subtraction',
    subject: 'Mathematics',
    level: 'Beginner'
  },
  {
    id: 2,
    title: 'Social Communication Skills',
    description: 'Interactive scenarios for practicing conversations',
    subject: 'Social Skills',
    level: 'Intermediate'
  },
  {
    id: 3,
    title: 'Reading Comprehension',
    description: 'Story-based activities with visual supports',
    subject: 'Language Arts',
    level: 'Advanced'
  }
])

const progressData = ref([
  { name: 'Math', progress: 60 },
  { name: 'Reading', progress: 75 },
  { name: 'Social', progress: 45 },
  { name: 'Motor', progress: 80 }
])

const studentAlerts = ref([
  {
    id: 1,
    type: 'warning',
    icon: '⚠️',
    studentName: 'Emma R.',
    message: 'showing signs of frustration in math lessons',
    suggestion: 'Suggestion: Try visual aids approach'
  },
  {
    id: 2,
    type: 'success',
    icon: '✅',
    studentName: 'Michael T.',
    message: 'exceeded reading comprehension goals',
    suggestion: 'Ready for advanced materials'
  }
])

const studentProgress = ref([
  {
    id: 1,
    name: 'Emma Rodriguez',
    avatar: '👧',
    grade: 'Grade 3',
    specialNeeds: 'Autism Spectrum',
    subjects: [
      { name: 'Math', progress: 65 },
      { name: 'Reading', progress: 45 },
      { name: 'Social Skills', progress: 30 }
    ]
  },
  {
    id: 2,
    name: 'Michael Thompson',
    avatar: '👦',
    grade: 'Grade 4',
    specialNeeds: 'ADHD',
    subjects: [
      { name: 'Math', progress: 80 },
      { name: 'Reading', progress: 90 },
      { name: 'Social Skills', progress: 70 }
    ]
  }
])

const resourceCategories = ref([
  {
    id: 'curriculum',
    icon: '📚',
    name: 'Curriculum Materials',
    description: 'Adaptive lesson plans and educational content',
    count: 245
  },
  {
    id: 'games',
    icon: '🎮',
    name: 'Interactive Games',
    description: 'Educational games for different learning needs',
    count: 89
  },
  {
    id: 'assessments',
    icon: '📊',
    name: 'Assessment Tools',
    description: 'Evaluation and progress tracking instruments',
    count: 67
  },
  {
    id: 'visual',
    icon: '🎨',
    name: 'Visual Aids',
    description: 'Charts, diagrams, and visual learning materials',
    count: 156
  }
])

const resources = ref([
  {
    id: 1,
    categoryId: 'curriculum',
    type: 'Lesson Plan',
    title: 'Visual Math: Addition with Objects',
    description: 'Step-by-step lesson plan for teaching addition using physical objects and visual aids',
    rating: 4.8,
    tags: ['Math', 'Visual Learning', 'Beginner']
  },
  {
    id: 2,
    categoryId: 'games',
    type: 'Interactive Game',
    title: 'Social Stories Adventure',
    description: 'Interactive game teaching social situations through story-based scenarios',
    rating: 4.6,
    tags: ['Social Skills', 'Interactive', 'Story-based']
  }
])

const discussionTopics = ref([
  {
    id: 1,
    avatar: '👩‍🏫',
    title: 'Best practices for autism spectrum support',
    preview: 'Looking for effective strategies for students with ASD...',
    replies: 12,
    timeAgo: '2 hours ago',
    category: 'Autism Support'
  },
  {
    id: 2,
    avatar: '👨‍🏫',
    title: 'Technology integration success stories',
    preview: 'Share your experiences with AI-assisted learning...',
    replies: 8,
    timeAgo: '1 day ago',
    category: 'Technology'
  }
])

const upcomingEvents = ref([
  {
    id: 1,
    day: '15',
    month: 'Dec',
    title: 'Special Needs Technology Workshop',
    description: 'Virtual workshop on latest assistive technologies',
    time: '2:00 PM - 4:00 PM'
  },
  {
    id: 2,
    day: '22',
    month: 'Dec',
    title: 'IEP Planning Masterclass',
    description: 'Advanced strategies for effective IEP development',
    time: '10:00 AM - 12:00 PM'
  }
])

const filteredResources = computed(() => {
  if (!selectedCategory.value) return []
  return resources.value.filter(resource => resource.categoryId === selectedCategory.value)
})

const selectCategory = (categoryId: string) => {
  selectedCategory.value = categoryId
}

const getCategoryName = (categoryId: string) => {
  const category = resourceCategories.value.find(cat => cat.id === categoryId)
  return category?.name || ''
}

const logout = () => {
  emit('logout')
}
</script>

<style scoped>
.portal-container {
  min-height: 100vh;
  background: #f8f9fa;
}

.portal-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
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
  gap: 1rem;
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
  background: white;
  padding: 0 2rem;
  display: flex;
  gap: 1rem;
  border-bottom: 1px solid #e0e0e0;
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
  color: #667eea;
  border-bottom-color: #667eea;
}

.nav-tab:hover {
  color: #667eea;
}

.tab-icon {
  font-size: 1.2rem;
}

.portal-content {
  padding: 2rem;
}

.tab-content {
  max-width: 1200px;
  margin: 0 auto;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  gap: 1rem;
}

.stat-icon {
  font-size: 2.5rem;
}

.stat-info h3 {
  margin: 0;
  font-size: 2rem;
  color: #333;
}

.stat-info p {
  margin: 0;
  color: #666;
  font-size: 0.9rem;
}

.dashboard-sections {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.section {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.section h3 {
  margin: 0 0 1.5rem 0;
  color: #333;
}

.activity-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.activity-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 10px;
}

.activity-avatar {
  font-size: 2rem;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #e9ecef;
  border-radius: 50%;
}

.activity-details p {
  margin: 0 0 0.25rem 0;
  font-size: 0.9rem;
}

.activity-time {
  font-size: 0.8rem;
  color: #666;
}

.task-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: #f8f9fa;
  border-radius: 8px;
}

.task-item input[type="checkbox"] {
  width: auto;
  margin: 0;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.content-header h2 {
  margin: 0;
  color: #333;
}

.lesson-tools {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.tool-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  text-align: center;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.tool-card:hover {
  transform: translateY(-5px);
}

.tool-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.tool-card h3 {
  margin: 0 0 1rem 0;
  color: #333;
}

.tool-card p {
  margin: 0 0 1.5rem 0;
  color: #666;
  line-height: 1.5;
}

.recent-lessons h3 {
  margin: 0 0 1.5rem 0;
  color: #333;
}

.lesson-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.lesson-card {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.lesson-card h4 {
  margin: 0 0 0.5rem 0;
  color: #333;
}

.lesson-card p {
  margin: 0 0 1rem 0;
  color: #666;
  font-size: 0.9rem;
}

.lesson-meta {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.lesson-subject,
.lesson-level {
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
}

.lesson-subject {
  background: #e3f2fd;
  color: #1976d2;
}

.lesson-level {
  background: #f3e5f5;
  color: #7b1fa2;
}

.lesson-actions {
  display: flex;
  gap: 0.5rem;
}

.btn-sm {
  padding: 0.5rem 1rem;
  font-size: 0.8rem;
}

.filter-controls {
  display: flex;
  gap: 1rem;
}

.filter-select {
  padding: 0.5rem 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
}

.progress-overview {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}

.progress-chart,
.student-alerts {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.chart-placeholder {
  display: flex;
  align-items: end;
  gap: 1rem;
  height: 200px;
  padding: 1rem 0;
}

.chart-bar {
  flex: 1;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 4px 4px 0 0;
  position: relative;
  min-height: 20px;
}

.bar-label {
  position: absolute;
  bottom: -25px;
  left: 50%;
  transform: translateX(-50%);
  font-size: 0.8rem;
  color: #666;
}

.alert-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem;
  border-radius: 10px;
  margin-bottom: 1rem;
}

.alert-item.warning {
  background: #fff3cd;
  border-left: 4px solid #ffc107;
}

.alert-item.success {
  background: #d4edda;
  border-left: 4px solid #28a745;
}

.alert-icon {
  font-size: 1.5rem;
}

.alert-suggestion {
  font-size: 0.8rem;
  color: #666;
  font-style: italic;
}

.detailed-progress {
  margin-top: 3rem;
}

.student-progress-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.student-card {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.student-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.student-avatar {
  font-size: 2rem;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8f9fa;
  border-radius: 50%;
}

.student-info h4 {
  margin: 0;
  color: #333;
}

.student-info p {
  margin: 0;
  color: #666;
  font-size: 0.9rem;
}

.progress-subjects {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.subject-progress {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.subject-name {
  min-width: 80px;
  font-weight: 600;
  color: #333;
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
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.progress-text {
  min-width: 40px;
  text-align: right;
  font-weight: 600;
  color: #667eea;
  font-size: 0.9rem;
}

.search-bar {
  display: flex;
  gap: 0.5rem;
}

.search-input {
  padding: 0.75rem 1rem;
  border: 1px solid #ddd;
  border-radius: 25px;
  width: 300px;
}

.search-btn {
  background: #667eea;
  color: white;
  border: none;
  padding: 0.75rem 1rem;
  border-radius: 25px;
  cursor: pointer;
}

.resource-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.category-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  text-align: center;
  transition: transform 0.3s ease;
  cursor: pointer;
}

.category-card:hover {
  transform: translateY(-5px);
}

.category-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.resource-count {
  display: block;
  margin-top: 1rem;
  color: #667eea;
  font-weight: 600;
  font-size: 0.9rem;
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.resource-item {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.resource-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.resource-type {
  background: #e3f2fd;
  color: #1976d2;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
}

.resource-rating {
  color: #ff9800;
  font-weight: 600;
}

.resource-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0;
}

.tag {
  background: #f0f0f0;
  color: #666;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
}

.resource-actions {
  display: flex;
  gap: 0.5rem;
}

.community-sections {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
}

.discussion-topics,
.community-events {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.topic-item {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  border-bottom: 1px solid #f0f0f0;
}

.topic-item:last-child {
  border-bottom: none;
}

.topic-avatar {
  font-size: 2rem;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8f9fa;
  border-radius: 50%;
  flex-shrink: 0;
}

.topic-content h4 {
  margin: 0 0 0.5rem 0;
  color: #333;
  font-size: 1rem;
}

.topic-content p {
  margin: 0 0 0.75rem 0;
  color: #666;
  font-size: 0.9rem;
}

.topic-meta {
  display: flex;
  gap: 1rem;
  font-size: 0.8rem;
  color: #999;
}

.topic-category {
  background: #e3f2fd;
  color: #1976d2;
  padding: 0.25rem 0.5rem;
  border-radius: 10px;
}

.event-item {
  display: flex;
  gap: 1rem;
  padding: 1.5rem;
  border-bottom: 1px solid #f0f0f0;
}

.event-item:last-child {
  border-bottom: none;
}

.event-date {
  text-align: center;
  background: #667eea;
  color: white;
  padding: 0.75rem;
  border-radius: 10px;
  min-width: 60px;
}

.date-day {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
}

.date-month {
  display: block;
  font-size: 0.8rem;
  opacity: 0.9;
}

.event-details h4 {
  margin: 0 0 0.5rem 0;
  color: #333;
}

.event-details p {
  margin: 0 0 0.5rem 0;
  color: #666;
  font-size: 0.9rem;
}

.event-time {
  font-size: 0.8rem;
  color: #999;
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
  
  .dashboard-sections,
  .progress-overview,
  .community-sections {
    grid-template-columns: 1fr;
  }
  
  .stats-grid {
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  }
  
  .content-header {
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
  }
  
  .search-bar {
    flex-direction: column;
  }
  
  .search-input {
    width: 100%;
  }
}
</style>