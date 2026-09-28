from fastmcp import FastMCP
from typing import Dict, Any

# Create the MCP server
mcp = FastMCP("Context Keeper")

# In-memory context store: user_id -> {topic, history}
contexts: Dict[str, Dict[str, Any]] = {}

@mcp.tool()
def start_context(user_id: str, topic: str) -> str:
    """Start a new context thread for a user."""
    contexts[user_id] = {"topic": topic, "history": []}
    return f"Context started for {user_id}: {topic}"

@mcp.tool()
def query_context(user_id: str) -> str:
    """Retrieve the current context thread for a user."""
    ctx = contexts.get(user_id)
    if not ctx:
        return "No active context for this user."
    return f"Current topic: {ctx['topic']}. History: {ctx['history']}"

@mcp.tool()
def list_contexts() -> str:
    """List all active context threads."""
    if not contexts:
        return "No active contexts."
    return "\n".join(f"{uid}: {c['topic']}" for uid, c in contexts.items())

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)