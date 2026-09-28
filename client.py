import asyncio
from fastmcp import Client

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
        # Start a context
        result = await client.call_tool("start_context", {
            "user_id": "demo_user",
            "topic": "roast chicken recipe"
        })
        print("START:", result.structured_content)

        # Query it back (separate call - this proves memory works)
        result = await client.call_tool("query_context", {
            "user_id": "demo_user"
        })
        print("QUERY:", result.structured_content)

        # List all contexts
        result = await client.call_tool("list_contexts", {})
        print("LIST:", result.structured_content)

asyncio.run(main())