import streamlit as st
from transformers import pipeline

# Load model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

skill_list = [
    "python","machine learning","deep learning","nlp",
    "sql","excel","power bi","tableau"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in skill_list if skill in text]

st.title("🧠 AI Resume Screening System")

resume_text = st.text_area("Paste Resume Text")

if st.button("Analyze Resume"):
    if resume_text:
        summary = summarizer(resume_text, max_length=60, min_length=25)[0]["summary_text"]
        skills = extract_skills(resume_text)

        st.subheader("🔍 AI Summary")
        st.write(summary)

        st.subheader("🛠 Extracted Skills")
        st.write(skills)
    else:
        st.warning("Please paste resume text")
