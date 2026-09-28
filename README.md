# Context Keeper

An MCP server that gives Alexa+ persistent context memory across interactions.

## Problem

Alexa+ is stateless by default. Ask a question, get an answer, and five
minutes later that context is gone. You have to repeat yourself. This is
a real friction point when using voice while cooking, working, or driving.

## Solution

Context Keeper is a self-hosted MCP server built with FastMCP (Python) that
maintains a lightweight per-user context thread across separate Alexa+
interactions. It uses the Streamable HTTP transport, spec 2025-11-25+.

## Tools Exposed

- `start_context(user_id, topic)` — begins a new context thread
- `query_context(user_id)` — retrieves the current context thread
- `list_contexts()` — lists all active context threads

## How It Works

The server registers three MCP tools via the `@mcp.tool()` decorator.
When an Alexa+ agent calls `query_context`, it receives the user's
current topic and history, then answers with continuity folded in.

## Run It

```bash
uv add fastmcp
uv run server.py