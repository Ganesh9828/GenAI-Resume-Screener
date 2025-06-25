import streamlit as st
from resume_parser import extract_text_from_pdf
from prompts import build_prompt
from utils import get_gpt_response, calculate_score

st.title("GenAI Resume Screener")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_description = st.text_area("Paste Job Description")

if uploaded_file and job_description:
    resume_text = extract_text_from_pdf(uploaded_file)
    prompt = build_prompt(resume_text, job_description)
    response = get_gpt_response(prompt)
    score = calculate_score(resume_text, job_description)

    st.subheader("Match Score:")
    st.write(score)
    st.subheader("GPT Feedback:")
    st.write(response)