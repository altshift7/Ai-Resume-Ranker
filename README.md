# 🧑‍💻 AI Resume Ranker  

An **AI-powered web application** that helps job seekers analyze how well their resume matches a job description.  
Upload your **resume (PDF)** and paste the job description, and the app will generate a **compatibility score using AI**.  

---

## 🚀 Features  

- 📄 Upload resume in **PDF format**  
- 📝 Paste job description directly  
- 🤖 AI-based compatibility scoring  
- 🎨 Clean and modern UI with a styled form  
- 📂 Resume upload handling with **Flask**  
- ⚡ Fast and lightweight design  

---

## 🛠️ Tech Stack  

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS  
- **AI Integration:** Hugging Face API  
- **PDF Processing:** PyMuPDF (`fitz`)  
- **Environment Management:** `venv`  

---

## 📂 Project Structure  
AI-Resume-Ranker/
│── app.py # Main Flask application
│── requirements.txt # Python dependencies
│── .env # API keys and environment variables
│── static/ # CSS & Images
│ ├── style.css
│ ├── bg.png
│ └── bg1.png
│── templates/ # HTML templates
│ └── index.html
│── uploads/ # Folder for uploaded resumes
│── README.md # Project documentation

<img width="538" height="617" alt="image" src="https://github.com/user-attachments/assets/b82fa4db-9cc5-42be-bbb2-5501367bf31d" />


---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/AI-Resume-Ranker.git
cd AI-Resume-Ranker

### 2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Set environment variables

Create a .env file in the project root and add your OpenAI API key:
OPENAI_API_KEY=your_api_key_here

### 5️⃣ Run the Flask app
python app.py

Now open http://127.0.0.1:5000/
 in your browser.

---

### 📸 Screenshots
<img width="1919" height="870" alt="image" src="https://github.com/user-attachments/assets/8457a081-c0e6-42db-b61d-f34db21123f7" />





