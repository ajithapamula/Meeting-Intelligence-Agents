# mcp/client.py
# Minimal MCP-style client facade. In real MCP, this would speak JSON-RPC.
# Here we keep it simple and call a local "tool server" registry.

from typing import Any, Dict
from mcp.server import ToolServer

class MCPClient:
    def __init__(self, server: ToolServer | None = None):
        # In real MCP, you'd connect over JSON-RPC/WebSocket/etc.
        # Here we host the tool server in-process for simplicity.
        self.server = server or ToolServer()

    def call(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call a tool by name with parameters.
        Returns a dict: {"ok": bool, "result": any, "error": str|None}
        """
        if tool_name not in self.server.tools:
            return {"ok": False, "result": None, "error": f"Unknown tool: {tool_name}"}
        try:
            result = self.server.tools[tool_name](**params)
            return {"ok": True, "result": result, "error": None}
        except Exception as e:
            return {"ok": False, "result": None, "error": str(e)}
