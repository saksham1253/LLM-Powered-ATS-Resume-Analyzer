from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import pdfplumber
import os

# ----------------------------
# Gemini API Setup
# ----------------------------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ----------------------------
# Gemini Response Function
# ----------------------------
def get_gemini_response(input_text, resume_text, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, resume_text, prompt])
    return response.text

# ----------------------------
# PDF Text Extractor
# ----------------------------
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text
    else:
        raise FileNotFoundError("No file uploaded")

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
}

/* Main title */
.main-title {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    color: black;
    margin-bottom: 25px;
}

/* Glass card style */
.glass-card {
    background: rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Upload box */
[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.25);
    border: 2px dashed #ff5e62;
    padding: 15px;
    border-radius: 12px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff512f, #dd2476);
    color: white;
    font-weight: 600;
    border-radius: 25px;
    padding: 12px 20px;
    width: 100%;
    border: none;
    transition: 0.3s ease-in-out;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ff9966, #ff5e62);
}
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Main Title
# ----------------------------
st.markdown('<h1 class="main-title">📊 ATS Resume Analyzer</h1>', unsafe_allow_html=True)

# ----------------------------
# Input Section
# ----------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
input_text = st.text_area("💼 Job Description Please......", key="input")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("📂 Upload Your Resume here....", type=["pdf"])
if uploaded_file is not None:
    st.success("✅ PDF uploaded Successfully")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Action Buttons with spacing
# ----------------------------
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    submit1 = st.button("📄 Review my resume")
with col2:
    submit2 = st.button("✨ How can I improvise my resume")
with col3:
    submit3 = st.button("📊 Percentage Match")

# ----------------------------
# Prompts
# ----------------------------
input_prompt1 = """
You are an experienced HR with tech experience in any one of the field of data science, machine learning, deep learning, data anlyst, web dev, your task is to review
the provided resume against the job description for these profiles.
Please share your professional evaluation on whether the candidate's profile
aligns with the job description or not.
Highlights the strengths and weaknesses of the applicant in relation to the 
specified job and make sure you doesn't give your title
"""

input_prompt2 = """
You are an experienced HR with tech experience in any one of the field of data science, machine learning, deep learning, data anlyst, web dev
your role is to scrutinize the resume in light of the job description provided.
share your insights on the candiddate's suitability for the role from an HR person
additionally, offer advice on enhancing the candidate's skills
and identify area of improvement.make sure you doesn't give your title
"""

input_prompt3 = """
You are an skilled ATS scanner with a deep understanding in one of the field of data science, machine learning, deep learning, data anlyst, web dev and deep ATS functionality.
your task is to evaluate the resume against the job description. Give me the percentage
of the matching of resume with the job description. first the output should come as percentage
and then keywords missing in the resume due to which the percentage score is less than 100.make sure you doesn't give your title
and give the percentage match in a very big font"""

# ----------------------------
# Actions
# ----------------------------
if submit1:
    if uploaded_file is not None:
        resume_text = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, resume_text, input_prompt1)
        st.subheader("📄 The Response is:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume first")

elif submit2:
    if uploaded_file is not None:
        resume_text = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, resume_text, input_prompt2)
        st.subheader("✨ The Response is:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume first")

elif submit3:
    if uploaded_file is not None:
        resume_text = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, resume_text, input_prompt3)
        st.subheader("📊 Percentage Match:")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume first")
