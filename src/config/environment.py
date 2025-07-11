from dotenv import load_dotenv

load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq

Anthropic_Model = ChatAnthropic(
 model="claude-3-haiku-20240307",
 temperature=0,
 max_tokens=1024,
 timeout=None,
 max_retries=2,
)

Gemini_Model = ChatGoogleGenerativeAI(
  model="gemini-2.0-flash",
  temperature=0,
  max_tokens=None,
  timeout=None,
  max_retries=2,
)

Groq_Model = ChatGroq(model="llama-3.1-8b-instant")  # cspell:ignore Groq


Tavily_tool = TavilySearch(
  topic="general",
  max_results=5,
)