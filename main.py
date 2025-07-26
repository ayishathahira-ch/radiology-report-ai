import streamlit as st
from app.voice_to_text import transcribe_audio
from app.text_to_report import generate_report_text
from app.generate_pdf import create_pdf

st.title("🩺 Radiology Report Generator (Voice to PDF)")
uploaded_audio = st.file_uploader("Upload radiologist dictation (WAV format)", type=["wav"])

if uploaded_audio:
    st.audio(uploaded_audio, format='audio/wav')
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_audio.read())

    st.info("Transcribing audio...")
    transcription = transcribe_audio("temp_audio.wav")
    st.success("Transcription Complete:")
    st.write(transcription)

    st.info("Generating structured report...")
    structured_text = generate_report_text(transcription)
    st.success("Formatted Report:")
    st.text(structured_text)

    if st.button("Download PDF"):
        pdf_file = create_pdf(structured_text)
        st.download_button("Download Report", data=pdf_file, file_name="scan_report.pdf")