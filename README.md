# AI Resume Ranker

A Flask web application that analyzes resumes against job descriptions using AI (Hugging Face API) to provide compatibility scores and feedback.

## Features

- PDF resume parsing using PyMuPDF
- AI-powered resume analysis using Hugging Face API
- Fallback analysis when API is unavailable
- Clean, responsive web interface
- Background image support

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your Hugging Face API key: