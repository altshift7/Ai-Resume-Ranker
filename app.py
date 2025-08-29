import os
import re
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash
import fitz  # PyMuPDF

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

# Hugging Face API configuration
HF_API_URL = "https://api-inference.huggingface.com/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
HF_API_KEY = os.getenv("HF_API_KEY")  

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from a PDF using PyMuPDF."""
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            # Ignore Pylance warning - get_text() method exists in PyMuPDF
            text += page.get_text()  # type: ignore
        return text
    except Exception as e:
        raise ValueError(f"Error reading PDF: {str(e)}")

def get_fit_score_and_feedback(resume_text: str, job_description: str) -> str:
    """
    Use Hugging Face API for resume ranking.
    """
    # Limit text length to avoid token limits
    resume_text = resume_text[:3000]
    job_description = job_description[:1500]
    
    prompt = f"""
You are an expert career advisor. Analyze the following resume and job description.
Provide:
- Fit Score: a number between 0 and 100
- Feedback: 3–5 sentences explaining the score and suggestions to improve.

Resume:
{resume_text}

Job Description:
{job_description}

Provide your response in this exact format:
Fit Score: [number between 0-100]
Feedback: [3-5 sentences of feedback]
"""

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 500,
            "temperature": 0.7,
            "return_full_text": False
        }
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if isinstance(result, list) and len(result) > 0:
            generated_text = result[0].get('generated_text', '')
            return generated_text.strip()
        else:
            return "Fit Score: 75\nFeedback: Using fallback analysis. For full functionality, please set up a Hugging Face API key with appropriate permissions."
    
    except requests.exceptions.RequestException:
        # Fallback to a simple scoring mechanism if API fails
        return fallback_analysis(resume_text, job_description)

def fallback_analysis(resume_text: str, job_description: str) -> str:
    """Fallback analysis if API is unavailable"""
    import random
    
    # Simple keyword matching
    keywords = ["python", "experience", "project", "develop", "skill", "team", "communication", "management", "analysis", "design"]
    matches = sum(1 for keyword in keywords if keyword in resume_text.lower() and keyword in job_description.lower())
    
    # Generate a score based on matches
    score = min(70 + (matches * 3), 95)
    
    feedbacks = [
        "The resume shows several relevant qualifications. Tailor it more specifically to the job description by highlighting key skills mentioned.",
        "Good overall match. Consider emphasizing more of the required technical skills and quantifiable achievements.",
        "Moderate alignment with the job requirements. Focus on adding keywords from the job description to improve ATS compatibility."
    ]
    
    return f"Fit Score: {score}\nFeedback: {random.choice(feedbacks)}"

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    feedback = None
    jd = None
    
    if request.method == "POST":
        file = request.files.get("resume")
        jd = request.form.get("job_description")

        if not file:
            flash("Please upload a resume file.", "error")
        elif not jd:
            flash("Please enter a job description.", "error")
        else:
            try:
                filename = file.filename or "uploaded_resume.pdf"
                filepath = os.path.join("uploads", filename)
                os.makedirs("uploads", exist_ok=True)
                file.save(filepath)

                resume_text = extract_text_from_pdf(filepath)
                result = get_fit_score_and_feedback(resume_text, jd)

                # Safely split result
                if "\n" in result:
                    score_line, feedback_text = result.split("\n", 1)
                else:
                    score_line, feedback_text = result, ""

                score = re.findall(r'\d+', score_line)
                score = score[0] if score else "N/A"
                feedback = feedback_text.replace("Feedback: ", "").strip()

            except Exception as e:
                flash(f"Error processing your request: {str(e)}", "error")

    return render_template("index.html", score=score, feedback=feedback, jd=jd)

if __name__ == "__main__":
    app.run(debug=True)