import { ref, computed } from 'vue'
import { 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword,
  signOut,
  onAuthStateChanged,
  User
} from 'firebase/auth'
import { doc, setDoc, getDoc } from 'firebase/firestore'
import { auth, db } from '../firebase/config'

interface UserProfile {
  uid: string
  email: string
  name: string
  role: 'student' | 'educator' | 'parent' | 'specialist'
  createdAt: Date
  lastLogin: Date
}

const currentUser = ref<User | null>(null)
const userProfile = ref<UserProfile | null>(null)
const isLoading = ref(false)
const error = ref<string | null>(null)

// Auth state observer
onAuthStateChanged(auth, async (user) => {
  currentUser.value = user
  if (user) {
    await loadUserProfile(user.uid)
  } else {
    userProfile.value = null
  }
})

const loadUserProfile = async (uid: string) => {
  try {
    const docRef = doc(db, 'users', uid)
    const docSnap = await getDoc(docRef)
    
    if (docSnap.exists()) {
      userProfile.value = docSnap.data() as UserProfile
    }
  } catch (err) {
    console.error('Error loading user profile:', err)
  }
}

const signIn = async (email: string, password: string) => {
  isLoading.value = true
  error.value = null
  
  try {
    const userCredential = await signInWithEmailAndPassword(auth, email, password)
    
    // Update last login
    if (userProfile.value) {
      await setDoc(doc(db, 'users', userCredential.user.uid), {
        ...userProfile.value,
        lastLogin: new Date()
      }, { merge: true })
    }
    
    return userCredential.user
  } catch (err: any) {
    error.value = err.message
    throw err
  } finally {
    isLoading.value = false
  }
}

const signUp = async (email: string, password: string, name: string, role: string) => {
  isLoading.value = true
  error.value = null
  
  try {
    const userCredential = await createUserWithEmailAndPassword(auth, email, password)
    
    // Create user profile in Firestore
    const profile: UserProfile = {
      uid: userCredential.user.uid,
      email,
      name,
      role: role as UserProfile['role'],
      createdAt: new Date(),
      lastLogin: new Date()
    }
    
    await setDoc(doc(db, 'users', userCredential.user.uid), profile)
    userProfile.value = profile
    
    return userCredential.user
  } catch (err: any) {
    error.value = err.message
    throw err
  } finally {
    isLoading.value = false
  }
}

const logout = async () => {
  try {
    await signOut(auth)
    userProfile.value = null
  } catch (err: any) {
    error.value = err.message
    throw err
  }
}

export const useAuthStore = () => {
  return {
    currentUser: computed(() => currentUser.value),
    userProfile: computed(() => userProfile.value),
    isLoading: computed(() => isLoading.value),
    error: computed(() => error.value),
    isAuthenticated: computed(() => !!currentUser.value),
    signIn,
    signUp,
    logout,
    clearError: () => { error.value = null }
  }
}