"""
Web related actions (search).
"""
import webbrowser
from typing import Tuple
import urllib.parse


def search_google(query: str) -> Tuple[bool, str]:
    """Open the default browser and search Google for `query`.

    Returns (success, message)
    """
    if not query:
        return False, "No query provided for search."
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)
    return True, f"Searching Google for {query}."
