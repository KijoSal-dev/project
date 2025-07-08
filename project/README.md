# AI Tutor for Special Needs Learners

A comprehensive Streamlit application designed to provide personalized learning experiences for students with special needs using free APIs and accessible design principles.

## Features

### 🎯 Core Functionality
- **Personalized Learning Paths**: Adaptive content based on individual needs and progress
- **Multi-Subject Support**: Reading, Math, Social Skills, Science, and Creative Arts
- **Progress Tracking**: Comprehensive analytics and achievement system
- **Interactive Quizzes**: Adaptive assessments with immediate feedback
- **AI Tutor Chat**: Conversational AI support for learning assistance

### ♿ Accessibility Features
- **Text-to-Speech**: Audio support for all content
- **High Contrast Mode**: Enhanced visibility for users with visual impairments
- **Large Text Options**: Adjustable font sizes
- **Simple Navigation**: Intuitive interface design
- **Visual Learning Aids**: Rich multimedia content support

### 🎮 Gamification
- **Achievement System**: Badges and rewards for progress milestones
- **Learning Games**: Interactive educational games
- **Progress Visualization**: Charts and graphs showing learning journey
- **Streak Tracking**: Daily learning habit encouragement

### 🔧 Technical Features
- **SQLite Database**: Local data storage for user progress
- **Free API Integration**: Uses free-tier APIs for content generation
- **Responsive Design**: Works on desktop and mobile devices
- **User Authentication**: Secure login and registration system

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ai-tutor-special-needs
```

2. Install required packages:
```bash
python -m pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

### Getting Started
1. **Register**: Create a new account with your learning preferences
2. **Login**: Access your personalized dashboard
3. **Choose Activities**: Select from various learning modules
4. **Track Progress**: Monitor your learning journey

### For Educators and Parents
- Monitor student progress through detailed analytics
- Customize learning preferences and difficulty levels
- Export progress data for external tracking
- Access comprehensive learning reports

### For Students
- Engage with interactive learning content
- Play educational games
- Chat with AI tutor for help
- Earn achievements and track progress

## API Integration

This application uses several free APIs:

### Content Generation
- **Hugging Face Inference API** (Free Tier): For generating educational content
- **OpenAI API** (Free Credits): Alternative for content generation
- **Google Gemini API** (Free Tier): For conversational AI features

### Text-to-Speech
- **ResponsiveVoice** (Free Tier): For audio content delivery
- **Google Cloud Text-to-Speech** (Free Tier): Alternative TTS service

### Educational Resources
- **Open Educational Resources**: Free educational content APIs
- **Khan Academy API**: Access to educational videos and exercises

## Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `password_hash`: Encrypted password
- `name`: Full name
- `age`: User age
- `learning_needs`: Special needs category
- `preferences`: JSON string of learning preferences
- `created_at`: Account creation timestamp

### Learning Sessions Table
- `id`: Primary key
- `user_id`: Foreign key to users
- `subject`: Learning subject
- `activity_type`: Type of activity completed
- `score`: Performance score
- `duration`: Session duration in minutes
- `completed_at`: Session completion timestamp

### Progress Table
- `id`: Primary key
- `user_id`: Foreign key to users
- `subject`: Subject area
- `skill`: Specific skill
- `level`: Current level
- `points`: Points earned
- `last_updated`: Last update timestamp

## Customization

### Adding New Subjects
1. Update the `FreeAPIs.get_educational_content()` method
2. Add new content templates
3. Update the subject selection options in the UI

### Modifying Difficulty Levels
1. Extend the difficulty options in content generation
2. Update quiz question templates
3. Adjust progress tracking algorithms

### Enhancing Accessibility
1. Add new accessibility features in `render_accessibility_controls()`
2. Implement additional visual/audio aids
3. Customize UI themes for specific needs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation wiki

## Acknowledgments

- Special thanks to the special needs education community
- Free API providers for making this project possible
- Streamlit team for the excellent framework
- Contributors and testers who helped improve accessibility

## Future Enhancements

- [ ] Integration with more AI APIs
- [ ] Advanced progress analytics
- [ ] Parent/teacher dashboard
- [ ] Mobile app version
- [ ] Multi-language support
- [ ] Advanced accessibility features
- [ ] Integration with educational standards
- [ ] Collaborative learning features