import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_notes(transcript: str) -> str:
    prompt = f"""
You are an AI project coordinator. From this meeting transcript, 
extract and organize all action items.

Your output must be structured into these sections:
1. **Tasks** → what needs to be done, and by whom.
2. **Decisions** → agreements made during the meeting.
3. **Deadlines** → important dates or commitments.

Format clearly using bullet points.

Transcript:
{transcript}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-4o for higher quality
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
