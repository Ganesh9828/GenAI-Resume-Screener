## GenAI-Resume-Screener


GenAI-Resume-Screener/
│
├── app.py                  
├── resume_parser.py       
├── job_description.txt     
├── prompts.py              
├── utils.py               
└── README.md

This is a GPT-powered Streamlit application that evaluates resumes against job descriptions and provides a compatibility score and qualitative feedback.

## Features
- Upload PDF resumes
- Match against a Job Description
- GPT-generated summary and match score
- Streamlit UI

## Tech Stack
- Python, Streamlit
- OpenAI API
- PyMuPDF / pdfminer

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements
streamlit
openai
PyMuPDF


## API Key
Add your OpenAI API key in utils.py before running.
