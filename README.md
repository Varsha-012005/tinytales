# 📚 Tiny Tales - AI-Powered Story Generator

Tiny Tales 
<img width="1920" height="986" alt="Screenshot 2026-02-25 134315" src="https://github.com/user-attachments/assets/5514aedc-50e3-4d31-add1-60e4baff086a" />
<img width="1920" height="964" alt="Screenshot 2026-02-25 134326" src="https://github.com/user-attachments/assets/e03f5d87-ca82-4d65-9c78-5c17d45d73b7" />
<img width="1920" height="962" alt="Screenshot 2026-02-25 134347" src="https://github.com/user-attachments/assets/ee3402bd-b927-42c0-af88-4e3b7316160c" />


Tiny Tales is a magical web application that transforms simple prompts into captivating stories using the power of AI. Whether you're a writer seeking inspiration, a teacher creating educational content, or just someone who loves creative storytelling, Tiny Tales makes story generation fun and accessible.

## ✨ Features

### 🤖 AI-Powered Story Generation
- Enter any prompt and watch as AI crafts a unique story
- Customize word count (50-1000 words) for stories of any length
- Choose from multiple genres: Fantasy, Sci-Fi, Mystery, Romance, Horror, Adventure, Comedy
- Intelligent story structuring with proper narrative flow

### 👤 User Management
- Secure registration and login system
- Password hashing with bcrypt for security
- Personal user profiles with creative statistics
- Track your story count, total words written, and average story length

### 📖 Story Library
- Save all generated stories to your personal collection
- Edit, delete, or update story metadata anytime
- Toggle public/private visibility with one click
- View reading time and word count for each story

### 🌍 Community Features
- Browse public stories from other users
- Filter stories by genre, author, or search content
- Discover new writers and creative works
- Build a community of storytellers

### 🔍 Advanced Filtering
- Search stories by content, title, or prompt
- Filter by genre (Fantasy, Sci-Fi, Mystery, etc.)
- Browse by specific authors
- Clear filters with one click

### 📱 Responsive Design
- Beautiful, responsive interface that works on all devices
- Warm, inviting color palette (cream, sage, blush, forest green)
- Smooth animations and hover effects
- Custom scrollbars for enhanced UX

## 🛠️ Tech Stack

### Backend
- **PHP** (>=7.4) - Core application logic
- **MySQL** - Database management
- **PDO** - Secure database connections with prepared statements
- **Python 3.11** - AI integration script
- **Ollama** - Local AI model server (TinyLlama)

### Frontend
- **HTML5** - Semantic structure
- **CSS3** - Custom properties, Flexbox, Grid, animations
- **JavaScript** - Vanilla JS for interactivity, AJAX calls
- **Font Awesome** - Icons for better UI
- **Google Fonts** - Inter & Playfair Display typography

### AI Integration
- **Python** script that communicates with Ollama API
- Configurable model parameters (temperature, context window)
- Retry logic with exponential backoff
- Comprehensive error handling and logging

## 📁 Project Structure

tiny-tales/

├── assets/

│ ├── style.css # Main stylesheet

│ ├── script.js # JavaScript functionality

│ └── img/ # Images and backgrounds

├── includes/

│ ├── config.php # Database configuration

│ └── exports/ # Exported stories directory

├── log/

│ └── debug.log # AI generation logs

├── models/

│ ├── User.php # User model class

│ ├── Story.php # Story model class

│ └── Share.php # Sharing functionality

├── public/

│ ├── auth.php # Login/register page

│ ├── dashboard.php # Main story generator

│ ├── stories.php # Story library

│ ├── profile.php # User profile

│ └── public.php # Public stories gallery

├── index.php # Landing page

├── generate.py # AI story generation script

└── README.md # This file

text

## 🗄️ Database Schema

### Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    bio TEXT,
    avatar VARCHAR(255),
    is_admin BOOLEAN DEFAULT FALSE,
    last_login TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

Stories Table
CREATE TABLE stories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    prompt TEXT NOT NULL,
    generated_text TEXT NOT NULL,
    word_count INT DEFAULT 100,
    genre VARCHAR(50),
    is_public BOOLEAN DEFAULT FALSE,
    reading_time INT DEFAULT 1,
    allow_comments BOOLEAN DEFAULT TRUE,
    is_deleted BOOLEAN DEFAULT FALSE,
    views INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

Supporting Tables
favorites - User story favorites

comments - Story comments

tags & story_tags - Story categorization

reading_history - User reading activity

user_preferences - User settings

story_exports - Export tracking

🚀 Installation & Setup

Prerequisites
Web server (Apache/Nginx) or XAMPP/WAMP/MAMP

PHP >= 7.4

MySQL

Python 3.11

Ollama (with TinyLlama model)

Step 1: Clone the Repository

git clone https://github.com/Varsha-012005/tinytales.git
cd tinytales
Step 2: Set Up the Database
Create a MySQL database named tiny_tales

Import the schema:

mysql -u root -p tiny_tales < docs/schema.sql
Step 3: Configure Database Connection
Edit includes/config.php with your database credentials:

php
$host = 'localhost';
$db = 'tiny_tales';
$user = 'root';
$pass = '';
Step 4: Install Python Dependencies
bash
pip install requests
Step 5: Install and Configure Ollama
Download and install Ollama from ollama.ai

Pull the TinyLlama model:

ollama pull tinyllama
Step 6: Configure Python Path
In public/dashboard.php, update the Python path to match your system:

$pythonPath = 'C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Python\\Python311\\python.exe';
Step 7: Set Directory Permissions
Ensure the log and exports directories are writable:

chmod -R 755 log/
chmod -R 755 includes/exports/
Step 8: Run the Application
Start your web server and MySQL

Start Ollama server

Navigate to http://localhost/tinytales

Register a new account and start creating stories!

How AI Story Generation Works
User Input - User enters a prompt, selects word count and genre

PHP Processing - Dashboard.php receives the request and validates input

Python Execution - PHP executes the Python script with parameters:

python generate.py "your prompt" 100 "Fantasy"
AI Generation - Python script communicates with Ollama's TinyLlama model

Retry Logic - Built-in retry mechanism (3 attempts) with delay

Error Handling - Comprehensive error logging to log/debug.log

Response Processing - Story returned to PHP, saved to database, displayed to user

Python Script Features
Configurable temperature (0.7) for creative output

Context window (512 tokens) for story coherence

Timeout handling (300 seconds) for long generations

Fallback mechanisms if AI service fails

 Security Features
Password Security: Passwords hashed with password_hash()

Session Management: Secure session handling with regeneration

SQL Injection: Prepared statements throughout

XSS Protection: Input sanitization with htmlspecialchars()

Access Control: Role-based permissions (admin/user)

Soft Delete: Stories marked as deleted, not permanently removed

Privacy Controls: Users control story visibility

 User Statistics
Total Stories - Number of stories created

Total Words - Cumulative word count across all stories

Average Length - Mean story length

Reading Time - Estimated reading time for each story

Last Login - Track user activity

Member Since - Account age

License
This project is licensed under the MIT License - see the LICENSE file for details.
