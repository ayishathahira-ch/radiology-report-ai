# 🩺 Radiology Report Generator

This app allows a radiologist to dictate scan results. The app transcribes the audio, generates a structured medical report using an LLM (GPT), and exports a PDF.

## Features
- 🎙 Voice-to-text using Google Cloud Speech-to-Text
- 🤖 Report formatting using GPT
- 📄 PDF generation
- 🚀 Streamlit web interface

## Setup
1. Set your Google credentials:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
streamlit run app/main.py
```

## Deployment Options
- Streamlit Cloud
- Google Cloud Run
- Heroku

**NOTE:** Do not commit credentials or sensitive data!