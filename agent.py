from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import calculator, web_search


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


agent = create_agent(
    model=llm,
    tools=[calculator, web_search],
    system_prompt="""You are an AI Research Assistant.

Use the calculator tool for mathematical calculations.
Use the web search tool when the user asks for current or up-to-date information.
For general questions that do not require tools, answer directly.

Give clear and concise answers."""
)