# mcp/tools.py
# A few realistic tools your agent can use right away.

import os
from datetime import datetime
from typing import List, Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "data", "reports")
OUTBOX_DIR = os.path.join(BASE_DIR, "data", "outbox")

os.makedirs(REPORTS_DIR, exist_ok=True)
os.makedirs(OUTBOX_DIR, exist_ok=True)

def save_report_tool(filename_prefix: str, notes: str, actions: str, summary: str) -> Dict[str, Any]:
    """
    Save a nice plaintext report to data/reports/<prefix>_<timestamp>.txt
    Returns file_path for downstream tools.
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_prefix = "".join(c for c in filename_prefix if c.isalnum() or c in ("-", "_"))[:40] or "report"
    file_path = os.path.join(REPORTS_DIR, f"{safe_prefix}_{ts}.txt")
    content = [
        "=== Meeting Report ===",
        "",
        "--- Notes ---",
        notes.strip(),
        "",
        "--- Action Items ---",
        actions.strip(),
        "",
        "--- Summary ---",
        summary.strip(),
        "",
    ]
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    return {"file_path": file_path}

def send_email_tool(to: List[str], subject: str, body: str, attachments: List[str] | None = None) -> Dict[str, Any]:
    """
    Simulated email sender. Writes a .eml-like file into data/outbox/.
    Useful to demo "agent -> tool -> corporate channel" without SMTP.
    """
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = os.path.join(OUTBOX_DIR, f"email_{ts}.txt")
    attachments = attachments or []
    payload = [
        f"To: {', '.join(to)}",
        f"Subject: {subject}",
        "",
        body,
        "",
        "Attachments:",
        *attachments
    ]
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(str(x) for x in payload))
    return {"status": "queued", "outbox_file": out_file}

def list_files_tool(dir_path: str) -> Dict[str, Any]:
    """List files in a directory (non-recursive)."""
    if not os.path.isdir(dir_path):
        raise FileNotFoundError(f"Not a directory: {dir_path}")
    files = sorted(os.listdir(dir_path))
    return {"files": files}

def read_file_tool(file_path: str) -> Dict[str, Any]:
    """Read a small text file (utf-8)."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Not a file: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return {"content": data}
