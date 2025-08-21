NOTE_PROMPT = """
You are a note-taking assistant. Extract the main discussion points from this meeting transcript.
Transcript:
{transcript}
"""

ACTION_PROMPT = """
You are an action-item assistant. Find all tasks, decisions, and deadlines in this meeting transcript.
Transcript:
{transcript}
"""

SUMMARY_PROMPT = """
You are a professional executive assistant. Summarize the meeting in 3-4 sentences, focusing on the outcome.
Transcript:
{transcript}
"""
