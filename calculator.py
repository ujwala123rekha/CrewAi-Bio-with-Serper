from crewai.tools import tool
from duckduckgo_search import DDGS

@tool
def search_web(query: str) -> str:
    """
    Useful for searching information about people or topics online.
    Input should be a search query.
    """

    try:
        results = DDGS().text(query, max_results=3)  # ⚡ limit results

        output = ""
        for r in results:
            output += r["body"] + "\n"

        return output

    except Exception:
        return "Error in web search"