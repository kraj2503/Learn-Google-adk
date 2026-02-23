# from google.adk.agents.llm_agent import Agent 
# from google.adk.agents import LlmAgent, BaseAgent, LoopAgent, SequentialAgent, ParallelAgent
# from google.adk.tools import AgentTool, FunctionTool, google_search
# import logging
# import sys
# # For config objects

# # --- Example Agent using a Llama 3 model deployed from Model Garden ---

# # Replace with your actual Vertex AI Endpoint resource name


# research_agent = Agent(
#     name="ResearchAgent",
#     model="gemini-2.5-flash-lite",
#     instruction="""You are a specialized research agent. Your only job is to use the
#     google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.""",
#     tools=[google_search],
#     output_key="research_findings", # The result of this agent will be stored in the session state with this key.
# )

# print("✅ research_agent created.")
# # Summarizer Agent: Its job is to summarize the text it receives.
# summarizer_agent = Agent(
#     name="SummarizerAgent",
#     model="gemini-2.5-flash-lite",
#     # The instruction is modified to request a bulleted list for a clear output format.
#     instruction="""Read the provided research findings: {research_findings}
# Create a concise summary as a bulleted list with 3-5 key points.""",
#     output_key="final_summary",
# )

# print("✅ summarizer_agent created.")
# # Root Coordinator: Orchestrates the workflow by calling the sub-agents as tools.
# # root_agent = Agent(
# #     name="ResearchCoordinator",
# #     model="gemini-2.5-flash-lite",
# #     # This instruction tells the root agent HOW to use its tools (which are the other agents).
# #     instruction="""You are a research coordinator. Your goal is to answer the user's query by orchestrating a workflow.
# # 1. First, you MUST call the `ResearchAgent` tool to find relevant information on the topic provided by the user.
# # 2. Next, after receiving the research findings, you MUST call the `SummarizerAgent` tool to create a concise summary.
# # 3. Finally, present the final summary clearly to the user as your response.""",
# #     # We wrap the sub-agents in `AgentTool` to make them callable tools for the root agent.
# #     tools=[
# #         AgentTool(research_agent),
# #         AgentTool(summarizer_agent)
# #     ],
# # )

# outline_agent = Agent(
#     name="OutlineAgent",
#     model="gemini-2.5-flash-lite",
#     instruction="""Create a blog outline for the given topic with:
#     1. A catchy headline
#     2. An introduction hook
#     3. 3-5 main sections with 2-3 bullet points for each
#     4. A concluding thought""",
#     output_key="blog_outline", # The result of this agent will be stored in the session state with this key.
# )

# print("✅ outline_agent created.")
# writer_agent = Agent(
#     name="WriterAgent",
#     model="gemini-2.5-flash-lite",
#     # The `{blog_outline}` placeholder automatically injects the state value from the previous agent's output.
#     instruction="""Following this outline strictly: {blog_outline}
#     Write a brief, 200 to 300-word blog post with an engaging and informative tone.""",
#     output_key="blog_draft", # The result of this agent will be stored with this key.
# )

# print("✅ writer_agent created.")
# editor_agent = Agent(
#     name="EditorAgent",
#     model="gemini-2.5-flash-lite",
#     # This agent receives the `{blog_draft}` from the writer agent's output.
#     instruction="""Edit this draft: {blog_draft}
#     Your task is to polish the text by fixing any grammatical errors, improving the flow and sentence structure, and enhancing overall clarity.""",
#     output_key="final_blog", # This is the final output of the entire pipeline.
# )

# print("✅ editor_agent created.")
# # root_agent = SequentialAgent(
# #     name="BlogPipeline",
# #     sub_agents=[outline_agent, writer_agent, editor_agent],
# # )

# # print("✅ Sequential Agent created.")


# tech_researcher = Agent(
#     name="TechResearcher",
#     model="gemini-2.5-flash-lite",
#     instruction="""Research the latest AI/ML trends. Include 3 key developments,
# the main companies involved, and the potential impact. Keep the report very concise (100 words).""",
#     tools=[google_search],
#     output_key="tech_research", # The result of this agent will be stored in the session state with this key.
# )

# print("✅ tech_researcher created.")
# # Health Researcher: Focuses on medical breakthroughs.
# health_researcher = Agent(
#     name="HealthResearcher",
#     model="gemini-2.5-flash-lite",
#     instruction="""Research recent medical breakthroughs. Include 3 significant advances,
# their practical applications, and estimated timelines. Keep the report concise (100 words).""",
#     tools=[google_search],
#     output_key="health_research", # The result will be stored with this key.
# )

# print("✅ health_researcher created.")

# # Finance Researcher: Focuses on fintech trends.
# finance_researcher = Agent(
#     name="FinanceResearcher",
#     model="gemini-2.5-flash-lite",
#     instruction="""Research current fintech trends. Include 3 key trends,
# their market implications, and the future outlook. Keep the report concise (100 words).""",
#     tools=[google_search],
#     output_key="finance_research", # The result will be stored with this key.
# )

# print("✅ finance_researcher created.")

# # The AggregatorAgent runs *after* the parallel step to synthesize the results.
# aggregator_agent = Agent(
#     name="AggregatorAgent",
#     model="gemini-2.5-flash-lite",
#     # It uses placeholders to inject the outputs from the parallel agents, which are now in the session state.
#     instruction="""Combine these three research findings into a single executive summary:

#     **Technology Trends:**
#     {tech_research}
    
#     **Health Breakthroughs:**
#     {health_research}
    
#     **Finance Innovations:**
#     {finance_research}
    
#     Your summary should highlight common themes, surprising connections, and the most important key takeaways from all three reports. The final summary should be around 200 words.""",
#     output_key="executive_summary", # This will be the final output of the entire system.
# )

# print("✅ aggregator_agent created.")

# # The ParallelAgent runs all its sub-agents simultaneously.
# parallel_research_team = ParallelAgent(
#     name="ParallelResearchTeam",
#     sub_agents=[tech_researcher, health_researcher, finance_researcher],
# )


# # This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
# # root_agent = SequentialAgent(
# #     name="ResearchSystem",
# #     sub_agents=[parallel_research_team, aggregator_agent],
# # )

# # print("✅ Parallel and Sequential Agents created.")


# initial_writer_agent = Agent(
#     name="InitialWriterAgent",
#     model="gemini-2.5-flash-lite",
#     instruction="""Based on the user's prompt, write the first draft of a short story (around 100-150 words).
#     Output only the story text, with no introduction or explanation.""",
#     output_key="current_story", # Stores the first draft in the state.
# )

# print("✅ initial_writer_agent created.")

# critic_agent = Agent(
#     name="CriticAgent",
#     model="gemini-2.5-flash-lite",
#     instruction="""You are a constructive story critic. Review the story provided below.
#     Story: {current_story}
    
#     Evaluate the story's plot, characters, and pacing.
#     - If the story is well-written and complete, you MUST respond with the exact phrase: "APPROVED"
#     - Otherwise, provide 2-3 specific, actionable suggestions for improvement.""",
#     output_key="critique", # Stores the feedback in the state.
# )

# print("✅ critic_agent created.")

# def exit_loop():
#     """Call this function ONLY when the critique is 'APPROVED', indicating the story is finished and no more changes are needed."""
#     return {"status": "approved", "message": "Story approved. Exiting refinement loop."}

# print("✅ exit_loop function created.")


# refiner_agent = Agent(
#     name="RefinerAgent",
#     model="gemini-2.5-flash-lite",
#     instruction="""You are a story refiner. You have a story draft and critique.
    
#     Story Draft: {current_story}
#     Critique: {critique}
    
#     Your task is to analyze the critique.
#     - IF the critique is EXACTLY "APPROVED", you MUST call the `exit_loop` function and nothing else.
#     - OTHERWISE, rewrite the story draft to fully incorporate the feedback from the critique.""",
    
#     output_key="current_story", # It overwrites the story with the new, refined version.
#     tools=[FunctionTool(exit_loop)], # The tool is now correctly initialized with the function reference.
# )

# story_refinement_loop = LoopAgent(
#     name="StoryRefinementLoop",
#     sub_agents=[critic_agent, refiner_agent],
#     max_iterations=10, # Prevents infinite loops
# )

# # The root agent is a SequentialAgent that defines the overall workflow: Initial Write -> Refinement Loop.
# root_agent = SequentialAgent(
#     name="StoryPipeline",
#     sub_agents=[initial_writer_agent, story_refinement_loop],
# )

# print("✅ Loop and Sequential Agents created.")


# print("✅ root_agent created.")



# ---------------

from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import InMemoryRunner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import google_search, AgentTool, ToolContext
from google.adk.code_executors import BuiltInCodeExecutor
import asyncio

print("✅ ADK components imported successfully.")


def show_python_code_and_result(response):
    for i in range(len(response)):
        # Check if the response contains a valid function call result from the code executor
        if (
            (response[i].content.parts)
            and (response[i].content.parts[0])
            and (response[i].content.parts[0].function_response)
            and (response[i].content.parts[0].function_response.response)
        ):
            response_code = response[i].content.parts[0].function_response.response
            if "result" in response_code and response_code["result"] != "```":
                if "tool_code" in response_code["result"]:
                    print(
                        "Generated Python Code >> ",
                        response_code["result"].replace("tool_code", ""),
                    )
                else:
                    print("Generated Python Response >> ", response_code["result"])


print("✅ Helper functions defined.")

retry_config = types.HttpRetryOptions(
    attempts=5,  # Maximum retry attempts
    exp_base=7,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)

# Pay attention to the docstring, type hints, and return value.
def get_fee_for_payment_method(method: str) -> dict:
    """Looks up the transaction fee percentage for a given payment method.

    This tool simulates looking up a company's internal fee structure based on
    the name of the payment method provided by the user.

    Args:
        method: The name of the payment method. It should be descriptive,
                e.g., "platinum credit card" or "bank transfer".

    Returns:
        Dictionary with status and fee information.
        Success: {"status": "success", "fee_percentage": 0.02}
        Error: {"status": "error", "error_message": "Payment method not found"}
    """
    # This simulates looking up a company's internal fee structure.
    fee_database = {
        "platinum credit card": 0.02,  # 2%
        "gold debit card": 0.035,  # 3.5%
        "bank transfer": 0.01,  # 1%
    }

    fee = fee_database.get(method.lower())
    if fee is not None:
        return {"status": "success", "fee_percentage": fee}
    else:
        return {
            "status": "error",
            "error_message": f"Payment method '{method}' not found",
        }


print("✅ Fee lookup function created")
print(f"💳 Test: {get_fee_for_payment_method('platinum credit card')}")
def get_exchange_rate(base_currency: str, target_currency: str) -> dict:
    """Looks up and returns the exchange rate between two currencies.

    Args:
        base_currency: The ISO 4217 currency code of the currency you
                       are converting from (e.g., "USD").
        target_currency: The ISO 4217 currency code of the currency you
                         are converting to (e.g., "EUR").

    Returns:
        Dictionary with status and rate information.
        Success: {"status": "success", "rate": 0.93}
        Error: {"status": "error", "error_message": "Unsupported currency pair"}
    """

    # Static data simulating a live exchange rate API
    # In production, this would call something like: requests.get("api.exchangerates.com")
    rate_database = {
        "usd": {
            "eur": 0.93,  # Euro
            "jpy": 157.50,  # Japanese Yen
            "inr": 83.58,  # Indian Rupee
        }
    }

    # Input validation and processing
    base = base_currency.lower()
    target = target_currency.lower()

    # Return structured result with status
    rate = rate_database.get(base, {}).get(target)
    if rate is not None:
        return {"status": "success", "rate": rate}
    else:
        return {
            "status": "error",
            "error_message": f"Unsupported currency pair: {base_currency}/{target_currency}",
        }


print("✅ Exchange rate function created")
print(f"💱 Test: {get_exchange_rate('USD', 'EUR')}")
# Currency agent with custom function tools
# root_agent = LlmAgent(
#     name="currency_agent",
#     model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
#     instruction="""You are a smart currency conversion assistant.

#     For currency conversion requests:
#     1. Use `get_fee_for_payment_method()` to find transaction fees
#     2. Use `get_exchange_rate()` to get currency conversion rates
#     3. Check the "status" field in each tool's response for errors
#     4. Calculate the final amount after fees based on the output from `get_fee_for_payment_method` and `get_exchange_rate` methods and provide a clear breakdown.
#     5. First, state the final converted amount.
#         Then, explain how you got that result by showing the intermediate amounts. Your explanation must include: the fee percentage and its
#         value in the original currency, the amount remaining after the fee, and the exchange rate used for the final conversion.

#     If any tool returns status "error", explain the issue to the user clearly.
#     """,
#     tools=[get_fee_for_payment_method, get_exchange_rate],
# )

# print("✅ Currency agent created with custom function tools")
# print("🔧 Available tools:")
# print("  • get_fee_for_payment_method - Looks up company fee structure")
# print("  • get_exchange_rate - Gets current exchange rates")


calculation_agent = LlmAgent(
    name="calculation_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    instruction="""You are a specialized calculator that ONLY responds with Python code. You are forbidden from providing any text, explanations, or conversational responses.
 
     Your task is to take a request for a calculation and translate it into a single block of Python code that calculates the answer.
     
     **RULES:**
    1.  Your output MUST be ONLY a Python code block.
    2.  Do NOT write any text before or after the code block.
    3.  The Python code MUST calculate the result.
    4.  The Python code MUST print the final result to stdout.
    5.  You are PROHIBITED from performing the calculation yourself. Your only job is to generate the code that will perform the calculation.
   
    Failure to follow these rules will result in an error.
       """,
    code_executor=BuiltInCodeExecutor(),  # Use the built-in Code Executor Tool. This gives the agent code execution capabilities
)

root_agent = LlmAgent(
    name="enhanced_currency_agent",
    model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
    # Updated instruction
    instruction="""You are a smart currency conversion assistant. You must strictly follow these steps and use the available tools.

  For any currency conversion request:

   1. Get Transaction Fee: Use the get_fee_for_payment_method() tool to determine the transaction fee.
   2. Get Exchange Rate: Use the get_exchange_rate() tool to get the currency conversion rate.
   3. Error Check: After each tool call, you must check the "status" field in the response. If the status is "error", you must stop and clearly explain the issue to the user.
   4. Calculate Final Amount (CRITICAL): You are strictly prohibited from performing any arithmetic calculations yourself. You must use the calculation_agent tool to generate Python code that calculates the final converted amount. This 
      code will use the fee information from step 1 and the exchange rate from step 2.
   5. Provide Detailed Breakdown: In your summary, you must:
       * State the final converted amount.
       * Explain how the result was calculated, including:
           * The fee percentage and the fee amount in the original currency.
           * The amount remaining after deducting the fee.
           * The exchange rate applied.
    """,
    tools=[
        get_fee_for_payment_method,
        get_exchange_rate,
        AgentTool(agent=calculation_agent),  # Using ano ther agent as a tool!
    ],
)

print("✅ Enhanced currency agent created")
print("🎯 New capability: Delegates calculations to specialist agent")
print("🔧 Tool types used:")
print("  • Function Tools (fees, rates)")
print("  • Agent Tool (calculation specialist)")

# async def main():
#     response = await root_agent.run_debug(
#         "Convert 1,250 USD to INR using a Bank Transfer. Show me the precise calculation."
#     )
#     print("response:", response)

# asyncio.run(main())