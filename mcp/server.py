# mcp/server.py
# Minimal in-process "MCP tool server" that registers callable tools.

from typing import Callable, Dict
from mcp.tools import (
    save_report_tool,
    send_email_tool,
    list_files_tool,
    read_file_tool,
)

class ToolServer:
    def __init__(self):
        self.tools: Dict[str, Callable] = {
            "save_report": save_report_tool,
            "send_email": send_email_tool,
            "list_files": list_files_tool,
            "read_file": read_file_tool,
        }
