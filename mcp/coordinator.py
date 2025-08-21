from agents.note_agent import extract_notes
from agents.action_agent import extract_actions
from agents.summary_agent import generate_summary
from mcp.client import MCPClient

class CoordinatorAgent:
    def __init__(self, transcript: str):
        self.transcript = transcript
        self.notes = None
        self.actions = None
        self.summary = None
        self.mcp = MCPClient()  # our MCP-style client

    def run(self, report_prefix: str = "meeting") -> dict:
        # Step 1: Extract Notes
        print("\n🤖 Running Notes Agent...")
        self.notes = extract_notes(self.transcript)

        # Step 2: Extract Actions
        print("\n🤖 Running Action Agent...")
        self.actions = extract_actions(self.transcript)

        # Step 3: Generate Summary
        print("\n🤖 Running Summary Agent...")
        self.summary = generate_summary(self.transcript)

        # Step 4: Save report via MCP tool
        print("\n🗂️  Saving report via MCP tool (save_report)...")
        save_res = self.mcp.call("save_report", {
            "filename_prefix": report_prefix,
            "notes": self.notes,
            "actions": self.actions,
            "summary": self.summary
        })
        if not save_res["ok"]:
            print(f"⚠️ save_report failed: {save_res['error']}")
            report_path = None
        else:
            report_path = save_res["result"]["file_path"]
            print(f"✅ Report saved: {report_path}")

        # Step 5: Simulate sending an email with the summary + attachment
        print("\n📧 Sending summary via MCP tool (send_email)...")
        email_res = self.mcp.call("send_email", {
            "to": ["team@example.com"],
            "subject": "Meeting Summary",
            "body": self.summary,
            "attachments": [report_path] if report_path else []
        })
        if not email_res["ok"]:
            print(f"⚠️ send_email failed: {email_res['error']}")
        else:
            print(f"✅ Email queued to outbox: {email_res['result']['outbox_file']}")

        return {
            "notes": self.notes,
            "actions": self.actions,
            "summary": self.summary,
            "report_path": report_path,
            "email_outbox": email_res["result"]["outbox_file"] if email_res["ok"] else None
        }
