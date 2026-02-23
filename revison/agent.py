from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.models import Gemini
from google.adk.agents import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.agent_tool import AgentTool
from google.genai import types
from google.adk.models.lite_llm import LiteLlm

# model = LiteLlm(model="openai/gpt-4o")

# MODEL_CHATGPT="GPT-4o mini"
# retry_config = types.HttpRetryOptions(
#     attempts=5,
#     exp_base=7,
#     initial_delay=1,
#     http_status_codes=[429, 500, 503, 504],
# )



model= Gemini(model="gemini-2.5-flash-lite")


script_writer_agent = LlmAgent(
    name="script_writer_agent",
    model=model,
    instruction="Research the topic and write a script. DO NOT include visual ideas, just the spoken script and hook.",
    tools=[google_search],
    output_key="generated_script"
)

# 2. Visualizer
visualizer_writer_agent = LlmAgent(
    name="visualizer_writer_agent",
    model=model,
    # Crucial change: Tell it WHERE to look
    instruction="Check the 'generated_script' in the state. Create a visual storyboard for every line of that script.",
    output_key="visual_concepts"
)

# 3. Formatter
formatter_agent = LlmAgent(
    name="formatter_agent",
    model=model,
    instruction="Combine the 'generated_script' and 'visual_concepts' into a final Markdown report. This is the END of the process.",
    output_key="final_short_concept"
)

# Root Agent - The "Manager"
root_agent = SequentialAgent(
    name="youtube_shorts_agent",
    # model=model,
    # instruction="""
    # You MUST execute these 3 steps in order for every user request:
    # STEP 1: Call 'script_writer_agent' with the user's topic.
    # STEP 2: Once Step 1 is done, call 'visualizer_writer_agent' to add visuals.
    # STEP 3: Finally, call 'formatter_agent' and SHOW THE FULL OUTPUT to the user.
    
    # IMPORTANT: Do not summarize. Do not ask for permission. Just run the tools one by one until the Markdown is finished.
    # """,
    sub_agents=[script_writer_agent, visualizer_writer_agent,formatter_agent],
)