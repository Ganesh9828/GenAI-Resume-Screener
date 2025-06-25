import openai

def get_gpt_response(prompt):
    openai.api_key = "your-api-key"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def calculate_score(resume, jd):
    # Simplified logic
    matches = sum(1 for word in jd.split() if word in resume)
    return round((matches / len(jd.split())) * 100, 2)