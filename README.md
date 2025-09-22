'''
## Meeting-Intelligence-Agents
=======
Meeting Intelligence Agent

Version: 1.0
Author: Ajitha
Project Type: Multi-Agent System + MCP Integration
Language: Python 3.10+
'''
## 📖 Project Overview
'''
The Meeting Intelligence Agent is a corporate productivity tool designed to process meeting transcripts and generate structured, actionable outputs. It uses a multi-agent system approach to handle different aspects of meeting intelligence:

Notes Extraction – Summarizes key discussion points.

Action Item Identification – Detects tasks, deadlines, and responsible members.

Summary Generation – Creates concise, human-readable meeting summaries.

MCP Integration – Simulates a Model Context Protocol for automating tasks like saving reports or sending emails.

Goal: Reduce repetitive manual work for managers, HR, or project teams, and provide instant meeting insights.
'''
## 🌟 Features
'''
Multi-Agent System

NoteAgent: Extracts key discussion points.

ActionAgent: Detects tasks, deadlines, and responsible team members.

SummaryAgent: Generates concise meeting summaries.

CoordinatorAgent: Orchestrates all agents and communicates with MCP tools.

MCP Tools

save_report: Saves structured reports automatically.

send_email: Simulates sending meeting summaries via email.

task_tracker: Tracks deadlines and actions.

Data Management

Stores structured reports, action items, and summaries in data/ folder.

Keeps sample transcripts for testing in data/sample_meetings/.

Live Input

Accepts live meeting transcripts entered via command line or text files.

Supports prefix/suffix tagging for project-specific meetings.

'''

## Sample Output:
'''
=== Meeting Intelligence Agent ===

Transcript:
Ajitha: We need to finish the quarterly report by Friday.
Bob: I’ll handle the financial section.
Carol: I’ll prepare the slides for the client presentation.

--- Notes ---
1. Deadline for quarterly report: Friday
2. Bob handles financial section
3. Carol prepares slides

--- Action Items ---
1. Finish quarterly report
2. Bob: Financial section
3. Carol: Slides

--- Summary ---
Quarterly report to be completed by Friday. Bob handles finance, Carol prepares slides. Review Thursday.

2️⃣ Live Input Mode

You can provide manual input instead of reading from a file:

python main.py --prefix "team-meeting" --input
'''
🛠 How It Works

1.CoordinatorAgent receives meeting transcript (live or file).

2.NoteAgent extracts discussion points.

3.ActionAgent identifies tasks, deadlines, and responsible members.

4.SummaryAgent produces concise summary.

5.MCP Client stores the report or sends notifications automatically.

                ┌─────────────┐
                │ Transcript  │
                └─────┬───────┘
                      │
             ┌────────▼─────────┐
             │ CoordinatorAgent │
             └────────┬─────────┘
          ┌───────────┼────────────┐
          │           │            │
    ┌─────▼─────┐ ┌───▼─────┐ ┌────▼────┐
    │ NoteAgent │ │ActionAgent│ │SummaryAgent│
    └───────────┘ └──────────┘ └───────────┘
          │           │            │
          └───────────┴────────────┘
                      │
               ┌──────▼──────┐
               │  MCP Client │
               └──────┬──────┘
                      │
             ┌────────▼─────────┐
             │ Save / Email /   │
             │ Task Tracker     │
             └─────────────────┘

✅ Career & Corporate Value

Reduces HR/management workload by automatically summarizing meetings.

Demonstrates multi-agent system design and automation integration (MCP).

Easily expandable to include real-time audio transcripts, email notifications, and dashboard integrations.

Strong resume project for AI/automation roles in corporate environments.

📦 Requirements

Python 3.10+

OpenAI API key (optional if integrating GPT models)

Standard libraries: os, sys, argparse, json

🛠 Future Enhancements

Real-time audio/video transcript integration

Multi-language meeting support

Dashboard for tasks, action items, and summaries

Automatic email delivery for all participants

Integration with corporate tools (Slack, Teams, Jira)

