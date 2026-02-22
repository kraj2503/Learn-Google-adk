
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search

from google.genai import types
from typing import List

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

# # ---- Intentionally pass incorrect datatype - `str` instead of `List[str]` ----
# def count_papers(papers: List[str]):
#     """
#     This function counts the number of papers in a list of strings.
#     Args:
#       papers: A list of strings, where each string is a research paper.
#     Returns:
#       The number of papers in the list.
#     """
#     return len(papers)


# Google Search agent
google_search_agent = LlmAgent(
    name="google_search_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    description="Analyse the github repositories and give feedback",
    instruction="""Use the google_search tool to find information and github repo from the link provided, then you will analyse the github repo and give all critics about the repo and ultimately rate it out of 10""",
    tools=[google_search]
)


# Root agent
root_agent = LlmAgent(
    name="research_paper_finder_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction="""Your task is to find Github Repositories online and analyze them 

    You MUST ALWAYS follow these steps:
    1) Find Github repo on the user provided link using the 'google_search_agent'. 
    """,
    tools=[AgentTool(agent=google_search_agent)] )