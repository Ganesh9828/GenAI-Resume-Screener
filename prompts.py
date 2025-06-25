def build_prompt(resume_text, job_description):
    return f"""
You are a resume screening assistant.

Job Description:
{job_description}

Resume:
{resume_text}

Analyze the resume against the job description and provide a score from 0 to 100, with justification.
"""