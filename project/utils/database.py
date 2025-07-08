"""
Database utilities for the AI Tutor application
"""

import sqlite3
import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import streamlit as st
from config import DATABASE_CONFIG

class DatabaseManager:
    """Manages all database operations"""
    
    def __init__(self, db_name: str = "ai_tutor.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Initialize database with all required tables"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create tables from config
        for table_name, table_config in DATABASE_CONFIG['tables'].items():
            columns_sql = ', '.join(table_config['columns'])
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})')
        
        conn.commit()
        conn.close()
    
    def hash_password(self, password: str) -> str:
        """Hash password for secure storage"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_user(self, username: str, password: str, name: str, age: int, 
                   learning_needs: str, preferences: List[str]) -> bool:
        """Create a new user account"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            password_hash = self.hash_password(password)
            preferences_json = json.dumps(preferences)
            
            cursor.execute('''
                INSERT INTO users (username, password_hash, name, age, learning_needs, preferences)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (username, password_hash, name, age, learning_needs, preferences_json))
            
            conn.commit()
            conn.close()
            return True
            
        except sqlite3.IntegrityError:
            return False
        except Exception as e:
            st.error(f"Database error: {e}")
            return False
    
    def authenticate_user(self, username: str, password: str) -> Optional[Dict]:
        """Authenticate user login"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            password_hash = self.hash_password(password)
            cursor.execute('''
                SELECT id, username, name, age, learning_needs, preferences
                FROM users WHERE username = ? AND password_hash = ?
            ''', (username, password_hash))
            
            user = cursor.fetchone()
            conn.close()
            
            if user:
                return {
                    'id': user[0],
                    'username': user[1],
                    'name': user[2],
                    'age': user[3],
                    'learning_needs': user[4],
                    'preferences': json.loads(user[5]) if user[5] else []
                }
            return None
            
        except Exception as e:
            st.error(f"Authentication error: {e}")
            return None
    
    def save_learning_session(self, user_id: int, subject: str, activity_type: str, 
                            score: int, duration: int) -> bool:
        """Save a completed learning session"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO learning_sessions (user_id, subject, activity_type, score, duration)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, subject, activity_type, score, duration))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            st.error(f"Error saving session: {e}")
            return False
    
    def update_progress(self, user_id: int, subject: str, skill: str, points: int) -> bool:
        """Update user progress in a subject/skill"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Check if progress record exists
            cursor.execute('''
                SELECT id, points, level FROM progress 
                WHERE user_id = ? AND subject = ? AND skill = ?
            ''', (user_id, subject, skill))
            
            existing = cursor.fetchone()
            
            if existing:
                new_points = existing[1] + points
                new_level = existing[2] + (1 if new_points >= existing[2] * 100 else 0)
                
                cursor.execute('''
                    UPDATE progress SET points = ?, level = ?, last_updated = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (new_points, new_level, existing[0]))
            else:
                cursor.execute('''
                    INSERT INTO progress (user_id, subject, skill, points)
                    VALUES (?, ?, ?, ?)
                ''', (user_id, subject, skill, points))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            st.error(f"Error updating progress: {e}")
            return False
    
    def get_user_progress(self, user_id: int) -> List[Dict]:
        """Get all progress data for a user"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT subject, skill, level, points, last_updated FROM progress 
                WHERE user_id = ? ORDER BY last_updated DESC
            ''', (user_id,))
            
            progress = cursor.fetchall()
            conn.close()
            
            return [{
                'subject': p[0], 
                'skill': p[1], 
                'level': p[2], 
                'points': p[3],
                'last_updated': p[4]
            } for p in progress]
            
        except Exception as e:
            st.error(f"Error getting progress: {e}")
            return []
    
    def get_learning_sessions(self, user_id: int, days: int = 30) -> List[Dict]:
        """Get recent learning sessions for a user"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cutoff_date = datetime.now() - timedelta(days=days)
            
            cursor.execute('''
                SELECT subject, activity_type, score, duration, completed_at 
                FROM learning_sessions 
                WHERE user_id = ? AND completed_at >= ?
                ORDER BY completed_at DESC
            ''', (user_id, cutoff_date.isoformat()))
            
            sessions = cursor.fetchall()
            conn.close()
            
            return [{
                'subject': s[0],
                'activity_type': s[1],
                'score': s[2],
                'duration': s[3],
                'completed_at': s[4]
            } for s in sessions]
            
        except Exception as e:
            st.error(f"Error getting sessions: {e}")
            return []
    
    def save_achievement(self, user_id: int, achievement_id: str) -> bool:
        """Save an earned achievement"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Check if achievement already exists
            cursor.execute('''
                SELECT id FROM achievements 
                WHERE user_id = ? AND achievement_id = ?
            ''', (user_id, achievement_id))
            
            if cursor.fetchone():
                conn.close()
                return False  # Already earned
            
            cursor.execute('''
                INSERT INTO achievements (user_id, achievement_id)
                VALUES (?, ?)
            ''', (user_id, achievement_id))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            st.error(f"Error saving achievement: {e}")
            return False
    
    def get_user_achievements(self, user_id: int) -> List[str]:
        """Get all achievements earned by a user"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT achievement_id FROM achievements 
                WHERE user_id = ?
            ''', (user_id,))
            
            achievements = cursor.fetchall()
            conn.close()
            
            return [a[0] for a in achievements]
            
        except Exception as e:
            st.error(f"Error getting achievements: {e}")
            return []
    
    def get_user_stats(self, user_id: int) -> Dict:
        """Get comprehensive user statistics"""
        try:
            progress_data = self.get_user_progress(user_id)
            sessions_data = self.get_learning_sessions(user_id)
            achievements_data = self.get_user_achievements(user_id)
            
            total_points = sum(p['points'] for p in progress_data)
            avg_level = sum(p['level'] for p in progress_data) / len(progress_data) if progress_data else 0
            subjects_count = len(set(p['subject'] for p in progress_data))
            total_sessions = len(sessions_data)
            avg_score = sum(s['score'] for s in sessions_data) / len(sessions_data) if sessions_data else 0
            total_time = sum(s['duration'] for s in sessions_data)
            
            # Calculate learning streak
            streak = self.calculate_learning_streak(user_id)
            
            return {
                'total_points': total_points,
                'average_level': round(avg_level, 1),
                'subjects_learning': subjects_count,
                'total_sessions': total_sessions,
                'average_score': round(avg_score, 1),
                'total_time_minutes': total_time,
                'learning_streak': streak,
                'achievements_count': len(achievements_data)
            }
            
        except Exception as e:
            st.error(f"Error getting user stats: {e}")
            return {}
    
    def calculate_learning_streak(self, user_id: int) -> int:
        """Calculate current learning streak in days"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Get distinct dates of learning sessions
            cursor.execute('''
                SELECT DISTINCT DATE(completed_at) as session_date
                FROM learning_sessions 
                WHERE user_id = ?
                ORDER BY session_date DESC
            ''', (user_id,))
            
            dates = [row[0] for row in cursor.fetchall()]
            conn.close()
            
            if not dates:
                return 0
            
            # Calculate streak
            streak = 0
            current_date = datetime.now().date()
            
            for date_str in dates:
                session_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                
                if session_date == current_date or session_date == current_date - timedelta(days=streak):
                    streak += 1
                    current_date = session_date
                else:
                    break
            
            return streak
            
        except Exception as e:
            st.error(f"Error calculating streak: {e}")
            return 0
    
    def get_leaderboard(self, limit: int = 10) -> List[Dict]:
        """Get top users by points for leaderboard"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT u.name, SUM(p.points) as total_points, COUNT(DISTINCT p.subject) as subjects
                FROM users u
                JOIN progress p ON u.id = p.user_id
                GROUP BY u.id, u.name
                ORDER BY total_points DESC
                LIMIT ?
            ''', (limit,))
            
            leaderboard = cursor.fetchall()
            conn.close()
            
            return [{
                'name': l[0],
                'total_points': l[1],
                'subjects': l[2],
                'rank': i + 1
            } for i, l in enumerate(leaderboard)]
            
        except Exception as e:
            st.error(f"Error getting leaderboard: {e}")
            return []
    
    def export_user_data(self, user_id: int) -> Dict:
        """Export all user data for download"""
        try:
            user_data = {
                'progress': self.get_user_progress(user_id),
                'sessions': self.get_learning_sessions(user_id, days=365),
                'achievements': self.get_user_achievements(user_id),
                'stats': self.get_user_stats(user_id),
                'export_date': datetime.now().isoformat()
            }
            
            return user_data
            
        except Exception as e:
            st.error(f"Error exporting data: {e}")
            return {}
    
    def cleanup_old_data(self, days: int = 365):
        """Clean up old session data (keep only recent data)"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cutoff_date = datetime.now() - timedelta(days=days)
            
            cursor.execute('''
                DELETE FROM learning_sessions 
                WHERE completed_at < ?
            ''', (cutoff_date.isoformat(),))
            
            deleted_count = cursor.rowcount
            conn.commit()
            conn.close()
            
            return deleted_count
            
        except Exception as e:
            st.error(f"Error cleaning up data: {e}")
            return 0