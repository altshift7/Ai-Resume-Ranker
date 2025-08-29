🚀 AI Resume Ranker - Smart Resume Analysis Tool
<div align="center">
https://img.shields.io/badge/Python-3.7%252B-3776AB?logo=python&logoColor=white
https://img.shields.io/badge/Flask-3.0-000000?logo=flask&logoColor=white
https://img.shields.io/badge/Hugging%2520Face-API-FFD21E?logo=huggingface&logoColor=black
https://img.shields.io/badge/License-MIT-yellow.svg
https://img.shields.io/github/stars/altshift7/Ai-Resume-Ranker?style=social

AI-powered resume analysis that matches your CV with job descriptions instantly

</div>
📖 Table of Contents
✨ Features

🚀 Quick Start

🛠️ Installation

📸 Demo

🏗️ Architecture

🤖 API Integration

🧪 Usage Examples

👥 Contributing

📄 License

🙋‍♂️ Support

✨ Features
🔥 Core Features
🤖 AI-Powered Analysis - Advanced resume-job matching using Hugging Face's Mixtral model

📄 PDF Resume Parsing - Extract text from PDF resumes with PyMuPDF

💯 Smart Scoring - Get compatibility scores (0-100) with detailed feedback

🎯 Actionable Insights - Receive specific suggestions to improve your resume

🛡️ Reliability Features
🔄 Fallback System - Works without API keys using intelligent keyword matching

🔒 Privacy First - Your resumes and data never leave your control

⚡ Real-time Processing - Instant analysis with smooth user experience

🎨 UI/UX Features
📱 Responsive Design - Works perfectly on desktop, tablet, and mobile

🎭 Modern Interface - Beautiful gradients and smooth animations

🌈 Custom Background - Professional background image support

🚀 Quick Start
Prerequisites
Python 3.7+

Git

Web browser

One-Command Installation
bash
# Clone and setup in one command
git clone https://github.com/altshift7/Ai-Resume-Ranker.git && cd Ai-Resume-Ranker && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
🎯 30-Second Setup
Clone the repo

bash
git clone https://github.com/altshift7/Ai-Resume-Ranker.git
cd Ai-Resume-Ranker
Install & run

bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
Open browser → http://localhost:5000

🛠️ Installation
Method 1: Basic Setup
bash
# 1. Clone repository
git clone https://github.com/altshift7/Ai-Resume-Ranker.git
cd Ai-Resume-Ranker

# 2. Create virtual environment
python -m venv .venv

# 3. Activate environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run application
python app.py
Method 2: With Hugging Face API (Recommended)
bash
# After basic setup, get your free API key:
# 1. Visit https://huggingface.co/settings/tokens
# 2. Create new token with 'read' permissions
# 3. Create .env file:
echo "HF_API_KEY=your_actual_api_key_here" > .env
echo "SECRET_KEY=your_random_secret_here" >> .env

# 4. Restart application for changes to take effect
📸 Demo
🎥 Live Demo
[Add your live demo link here once deployed]

📋 Sample Output
text
✅ Fit Score: 87/100
📝 Feedback: Strong match! Your resume shows excellent relevant experience in 
Python development and cloud technologies. Consider highlighting more specific 
project achievements and metrics to further strengthen your application.
🖼️ Application Preview
(Add screenshots of your application here)

<!-- ![Main Interface](screenshots/main.png) ![Results Page](screenshots/results.png) -->
🏗️ Architecture
<img width="923" height="518" alt="image" src="https://github.com/user-attachments/assets/af0e20ec-a134-474e-90cb-3124af955bba" />




📁 Project Structure
text
Ai-Resume-Ranker/
├── app.py                 # 🎯 Main Flask application
├── requirements.txt       # 📦 Dependencies
├── .env.example          # ⚙️ Environment template
├── .gitignore           # 🙈 Git ignore rules
├── README.md            # 📖 This file
├── static/              # 🎨 Frontend assets
│   ├── style.css        # 💄 Stylesheet
│   └── bg.png          # 🖼️ Background image
├── templates/           # 🎭 HTML templates
│   └── index.html       # 🏠 Main page
├── typings/             # 📝 Type definitions
│   └── fitz/
│       └── __init__.pyi 
└── uploads/             # 📁 User uploads (gitignored)
🤖 API Integration
Hugging Face Setup
Free Account: Create at huggingface.co/join

Generate Token: Visit settings/tokens

Configure: Add to your .env file:

env
HF_API_KEY=hf_your_actual_token_here
SECRET_KEY=generate_random_secret_here
🔄 Fallback Mode
No API key? No problem! The system automatically uses:

Keyword matching algorithm

Skill-based scoring

Industry-standard resume evaluation criteria

🧪 Usage Examples
Example 1: Software Developer Resume
python
# Input: Python Developer resume + Job description
# Output: 
# Score: 92/100
# Feedback: "Excellent Python and Django experience. Highlight more AWS projects."
Example 2: Marketing Professional
python
# Input: Marketing resume + Job description  
# Output:
# Score: 78/100
# Feedback: "Strong digital marketing skills. Add more metrics to campaign results."
Example 3: Career Changer
python
# Input: Career change resume + Job description
# Output:
# Score: 65/100  
# Feedback: "Focus on transferable skills. Consider adding relevant certifications."
👥 Contributing
We welcome contributions! Here's how you can help:

🎯 First Time Contributors
Fork the repository

Create a feature branch: git checkout -b feature/amazing-feature

Make your changes

Test thoroughly: python app.py

Submit a pull request

📋 Development Guidelines
Write clear commit messages

Update documentation when needed

Test changes on multiple resume types

Follow PEP 8 coding standards

🚀 Planned Features
Multi-format support (DOCX, TXT)

Resume template generator

Export analysis reports

Batch processing

Advanced analytics dashboard

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙋‍♂️ Support
📚 Documentation
Flask Documentation

Hugging Face API Docs

PyMuPDF Documentation

🐛 Bug Reports
Found an issue? Open a GitHub Issue

💬 Community
🌟 Star this repo if you find it useful!

🔄 Share with your network

🐛 Report issues and suggest features

📊 Project Stats
https://img.shields.io/github/forks/altshift7/Ai-Resume-Ranker?style=social
https://img.shields.io/github/issues/altshift7/Ai-Resume-Ranker
https://img.shields.io/github/issues-pr/altshift7/Ai-Resume-Ranker

<div align="center">
Made with ❤️ by Your Name

If this project helped your job search, consider giving it a ⭐!

https://img.shields.io/github/stars/altshift7/Ai-Resume-Ranker?style=social

</div>
🔗 Quick Links
💻 Live Demo (Add your deployment link here)

🐛 Report Bug

💡 Request Feature

📧 Contact

🎉 Acknowledgments
Hugging Face for their amazing AI models

Flask community for the excellent web framework

PyMuPDF developers for PDF processing capabilities

This README is dynamically updated. Last update: ${new Date().toLocaleDateString()}
