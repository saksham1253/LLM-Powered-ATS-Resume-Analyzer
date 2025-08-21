# LLM-Powered-ATS-Resume-Analyzer
The **ATS Resume Analyzer** is a web-based application built using **Streamlit** and powered by **Google Generative AI (Gemini)**. This project utilizes **Large Language Models (LLMs)** to evaluate resumes against job descriptions, providing insightful analysis, improvement suggestions, and ATS-style percentage matching.  

---

## 📌 Features  
- **Resume Upload (PDF)** – Upload resumes directly in PDF format.  
- **Job Description Input** – Paste the desired job description for analysis.  
- **Professional Resume Review** – Receive a detailed evaluation highlighting strengths and weaknesses.  
- **Improvement Suggestions** – Get tailored recommendations to enhance resume alignment with job requirements.  
- **Percentage Match Score** – ATS-style scoring with missing keywords identified.  

---

## 🛠️ Technology Stack  
- **Python**  
- **Streamlit** – Interactive web application framework.  
- **Google Generative AI (Gemini LLM)** – For resume analysis and recommendations.  
- **pdf2image, PIL** – PDF and image preprocessing.  

---

## 🎯 Objective  
The primary goal of this project is to assist job seekers in improving their resumes for better alignment with job descriptions. By leveraging **LLM-powered analysis**, this tool helps candidates:  
- Increase the likelihood of passing **Applicant Tracking System (ATS)** screenings.  
- Identify missing keywords and skills.  
- Present a more competitive resume to recruiters.  

---

## ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/saksham1253/LLM-Powered-ATS-Resume-Analyzer.git
   cd LLM-Powered-ATS-Resume-Analyzer
2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

---

## Set up of Environment Variables

- Create a **.env** file in the root directory.
- Add your Google API Key in **.env** file:
   ```bash
   GOOGLE_API_KEY=your_api_key_here

---

## Run the Streamlit Application

- Write this in the terminal
   ```bash
   streamlit run app.py

---

## 📂 Project Structure

📦 ATS Resume Analyzer
├── 📄 app.py                # Main Streamlit application
├── 📄 requirements.txt      # Python dependencies
├── 📄 .env                  # API Key (not pushed to GitHub)
└── 📄 README.md             # Project documentation

---

## Future Improvements

- Support for multiple resume formats (DOCX, TXT).
- More advanced keyword extraction and ranking.
- Multi-job comparison feature.
- Deployment on cloud (Streamlit Cloud, GCP, or AWS).

---

## Contributing

**Contributions are welcome. Please fork the repository and submit a pull request for any enhancements or bug fixes**.



   
