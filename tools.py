from langchain_core.tools import tool
from ddgs import DDGS
from simpleeval import simple_eval


@tool
def calculator(expression: str) -> str:
    """Calculates the result of a mathematical expression."""
    try:
        return str(simple_eval(expression))
    except Exception as e:
        return f"Error occurred while calculating: {e}"


@tool
def web_search(query: str) -> str:
    """Searches the web for current information."""
    results = DDGS().text(query, max_results=5)
    return str(results)