Tiny Tales - AI-Powered Story Generator

Tiny Tales is an AI-powered story generation platform that transforms your ideas into captivating stories using local AI models. Whether you're a writer seeking inspiration, a teacher creating educational content, or just someone who loves stories, Tiny Tales helps you create unique tales in seconds.

 Core Features
Story Generation
 AI-Powered Creation: Generate stories using Ollama's TinyLlama model

 Custom Prompts: Start with any idea, sentence, or keywords

 Word Count Control: Set desired length (50-1000 words)

 Genre Selection: Choose from Fantasy, Sci-Fi, Mystery, Romance, Horror, Adventure, Comedy

 Real-time Generation: Watch your story come to life instantly

User Features
 User Authentication: Secure login and registration system

 Story Library: Save and manage all your generated stories

 Search & Filter: Find stories by title, content, or genre

 Public Stories: Share your creations with the community

 Favorites: Bookmark stories you love

 Comments: Engage with other users' stories

Story Management
 Read Stories: Beautiful reading interface with word count and reading time

 Edit Stories: Modify and refine your generated content

 Tag System: Organize stories with custom tags

 Privacy Controls: Make stories public or keep them private

 Export Options: Download stories as TXT or PDF

 Soft Delete: Remove stories without permanent loss

 Technology Stack
Backend
PHP 8.0+ - Core application logic

MySQL 5.7+ - Database management

Python 3.8+ - AI integration layer

Ollama - Local LLM server with TinyLlama model

Frontend
HTML5/CSS3 - Responsive interface

JavaScript (ES6) - Interactive features

Font Awesome 6 - Icons and visual elements

Google Fonts - Inter & Playfair Display fonts

AI Integration
TinyLlama - Lightweight 1.1B parameter model

Ollama API - Local model serving

Python Scripts - Story generation logic


 Database Schema
Table	Purpose
users	User accounts and authentication
stories	Generated stories with metadata
favorites	User's favorite stories
tags	Story categorization
story_tags	Many-to-many tag relationships
comments	User comments on stories
reading_history	Track user reading activity
story_exports	Record of exported stories
user_preferences	User settings and defaults
Key Features:

Full-text search indexes on stories

Soft delete capability

Reading time calculation

Export tracking

 Installation in 6 Steps
Prerequisites
PHP 8.0 or higher

MySQL 5.7 or higher

Python 3.8 or higher

Ollama installed and running

Apache/Nginx web server

Step 1: Clone & Setup
git clone https://github.com/yourusername/tinytales.git
cd tinytales
Step 2: Create Database
# Create database and tables
mysql -u root -p < docs/schema.sql
Step 3: Configure Database
Edit includes/config.php:

$host = 'localhost';
$db   = 'tiny_tales';
$user = 'root';
$pass = 'your_password';
Step 4: Install & Start Ollama

# Install Ollama from https://ollama.ai
# Pull TinyLlama model
ollama pull tinyllama

# Ensure Ollama is running (default: http://localhost:11434)
Step 5: Configure Python Path
In public/dashboard.php, update the Python path:


$pythonPath = 'C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\python.exe';
Step 6: Set Permissions

# Create necessary directories
mkdir -p includes/exports log
chmod -R 755 includes/exports log
🔧 Python Script Details
generate.py Features
Retry Logic: 3 attempts with delay on failure

Error Handling: Comprehensive error catching

Timeout Protection: 300-second timeout for long generations

Fallback Stories: Returns helpful message on failure

Logging: Detailed logging to log/debug.log

Parameters:

python
prompt = sys.argv[1]      # Story prompt/idea
word_count = sys.argv[2]   # Desired length
genre = sys.argv[3]        # Story genre (optional)
 Security Features
Feature	Implementation
Password Security	Bcrypt hashing
Session Management	PHP sessions with regeneration
SQL Injection	PDO prepared statements
XSS Prevention	HTML special characters encoding
CSRF Protection	Session-based tokens
Input Validation	Sanitization on all inputs
Soft Delete	Stories flagged, not permanently deleted
 User Roles
Regular Users
Generate stories with AI

Save stories to personal library

Make stories public/private

Comment on public stories

Favorite stories

Export stories as TXT/PDF

Admin Users
All regular user features

Manage all stories

View system logs

Monitor generation activity

🎮 User Flow
Story Generation
Login → Access dashboard

Enter Prompt → Describe your story idea

Set Options → Choose word count and genre

Generate → AI creates unique story

Save → Store in your library

Share → Make public for community

Community Engagement
Browse → Explore public stories

Filter → Search by genre, author, keywords

Read → View full stories

Interact → Favorite and comment

Discover → Find inspiration from others

 Troubleshooting
Common Issues
Python Generation Fails

Verify Ollama is running: http://localhost:11434

Check Python path in dashboard.php

Review log/debug.log for errors

Database Connection Errors

Verify MySQL is running

Check credentials in config.php

Ensure database exists

Export Directory Issues

Check write permissions on includes/exports/

Verify disk space availability
