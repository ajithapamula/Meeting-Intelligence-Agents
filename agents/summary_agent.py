import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(transcript: str) -> str:
    prompt = f"""
    You are an AI assistant writing an executive meeting summary.
Write a concise, professional recap (3–4 sentences) covering:

- Meeting purpose
- Key outcomes
- Next steps / deadlines

Avoid jargon. Be clear, neutral, and professional.

Transcript:



    {transcript}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response.choices[0].message.content.strip()
