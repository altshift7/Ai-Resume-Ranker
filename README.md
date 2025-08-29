AI Resume Ranker 🤖📄

An intelligent web application that analyzes resumes against job descriptions using AI to provide compatibility scores and personalized feedback.
Ideal for job seekers who want to optimize their resumes for specific roles.

✨ Features

📄 PDF Resume Parsing – Extract text using PyMuPDF

🤖 AI-Powered Analysis – Hugging Face Mixtral model for intelligent job matching

💯 Compatibility Scoring – Get a 0–100 score with actionable feedback

🔄 Fallback System – Works without API keys via keyword matching

🎨 Beautiful UI – Modern, responsive design with background image support

🔒 Privacy Focused – Resumes and API keys remain local & private

🚀 Quick Start
Prerequisites

Python 3.7+

Git

Web browser

Installation
# Clone the repository
git clone https://github.com/altshift7/Ai-Resume-Ranker.git
cd Ai-Resume-Ranker

# Create a virtual environment
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Environment Setup
# Copy example env file
cp .env.example .env

# Edit .env and add your keys
HF_API_KEY=your_huggingface_api_key_here
SECRET_KEY=your_flask_secret_key_here


🔑 Hugging Face API Key (optional):

Create a free account on Hugging Face

Generate a Read token in Access Tokens

Paste it in .env

If no key is provided, the app falls back to keyword-based matching.

Run the App
python app.py


Then open 👉 http://localhost:5000
 in your browser.

📸 Screenshots

(Add screenshots here once available)

<!-- ![Main Interface](screenshots/main.png) ![Results Page](screenshots/results.png) -->
🛠 Tech Stack

Backend: Flask (Python)

AI Integration: Hugging Face Inference API (Mixtral-8x7B-Instruct-v0.1)

PDF Processing: PyMuPDF (fitz)

Frontend: HTML5, CSS3, JavaScript

Styling: Modern CSS with gradients & animations

Env Management: python-dotenv

📁 Project Structure
Ai-Resume-Ranker/
├── app.py              # Main Flask app
├── requirements.txt    # Dependencies
├── .env.example        # Env variables template
├── .gitignore          # Ignore rules
├── README.md           # Documentation
├── static/             # CSS, images
├── templates/          # HTML templates
├── typings/            # PyMuPDF type definitions
└── uploads/            # User-uploaded resumes (ignored by git)

🎯 How It Works

PDF Extraction – Resume text extracted via PyMuPDF

AI Analysis – Resume & job description sent to Hugging Face API

Scoring – Returns compatibility score (0–100)

Feedback – AI + keyword analysis → actionable improvement tips

🤝 Contributing

We welcome contributions!

🐛 Report issues

💡 Suggest features

📝 Improve docs

🔧 Submit PRs

Dev Workflow:

git checkout -b feature/amazing-feature
git commit -m "Add amazing feature"
git push origin feature/amazing-feature


Open a Pull Request 🚀

📄 License

This project is licensed under the MIT License
.

⚠️ Disclaimer

This tool provides AI-generated suggestions only. Always:

Review feedback critically

Treat it as guidance, not absolute truth

Avoid uploading sensitive/confidential data

🌟 Star History

🚧 Roadmap

 Multi-file format support (DOCX, TXT)

 Resume template suggestions

 Export analysis results

 Batch resume processing

 Advanced AI model selection

 Performance optimization
