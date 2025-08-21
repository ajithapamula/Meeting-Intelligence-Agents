import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_actions(transcript: str) -> str:
    prompt = f"""
    You are a professional meeting note-taker for a corporate team. 
Read the transcript and write clean, structured notes.

Guidelines:
- Capture only the main discussion points.
- Remove small talk or irrelevant details.
- Group related points together.
- Use short, clear sentences in bullet points.

Transcript:
    {transcript}
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
