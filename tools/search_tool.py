from __future__ import annotations

"""Provides a web search tool backed by DuckDuckGo for agents.  Falls back
to a stub implementation if dependencies are missing."""
from crewai.tools import tool

try:
    from langchain_community.tools import DuckDuckGoSearchRun
    _ddg = DuckDuckGoSearchRun()

    @tool("Web Search")
    def web_search_tool(query: str) -> str:
        """
        Search the web for current information on a topic.
        Input: a concise search query string.
        Returns: a text summary of the top search results.
        """
        try:
            return _ddg.run(query)
        except Exception as e:
            return f"Search failed: {e}. Try rephrasing the query."

except ImportError:
    @tool("Web Search (unavailable)")
    def web_search_tool(query: str) -> str:
        """Stub — install duckduckgo-search and langchain-community to enable."""
        return (
            f"Web search unavailable. "
            f"Run: pip install duckduckgo-search langchain-community\n"
            f"Query was: {query}"
        )
