import uuid
from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from google.adk.apps.app import App, ResumabilityConfig
from google.adk.tools.function_tool import FunctionTool

from IPython.display import display, Image as IPImage
import base64


# retry_config = types.HttpRetryOptions(
#     attempts=5,  # Maximum retry attempts
#     exp_base=7,  # Delay multiplier
#     initial_delay=1,
#     http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
# )

# #  MCP integration with Everything Server
# mcp_image_server = McpToolset(
#     connection_params=StdioConnectionParams(
#         server_params=StdioServerParameters(
#             command="npx",  # Run MCP server via npx
#             args=[
#                 "-y",  # Argument for npx to auto-confirm install
#                 "@modelcontextprotocol/server-everything",
#             ],
#             tool_filter=["getTinyImage"],
#         ),
#         timeout=30,
#     )
# )

# root_agent = LlmAgent(
#     model=Gemini(model="gemini-2.5-flash-lite", retry_options=retry_config),
#     name="image_agent",
#     instruction="Use the MCP Tool to generate images for user queries",
#     tools=[mcp_image_server],
# )


# for event in response:
#     if event.content and event.content.parts:
#         for part in event.content.parts:
#             if hasattr(part, "function_response") and part.function_response:
#                 for item in part.function_response.response.get("content", []):
#                     if item.get("type") == "image":
#                         display(IPImage(data=base64.b64decode(item["data"])))

# print("✅ MCP Tool created")

# LARGE_ORDER_THRESHOLD = 5


# def place_shipping_order(
#     num_containers: int, destination: str, tool_context: ToolContext
# ) -> dict:
#     """Places a shipping order. Requires approval if ordering more than 5 containers (LARGE_ORDER_THRESHOLD).

#     Args:
#         num_containers: Number of containers to ship
#         destination: Shipping destination

#     Returns:
#         Dictionary with order status
#     """

#     # -----------------------------------------------------------------------------------------------
#     # -----------------------------------------------------------------------------------------------
#     # SCENARIO 1: Small orders (≤5 containers) auto-approve
#     if num_containers <= LARGE_ORDER_THRESHOLD:
#         return {
#             "status": "approved",
#             "order_id": f"ORD-{num_containers}-AUTO",
#             "num_containers": num_containers,
#             "destination": destination,
#             "message": f"Order auto-approved: {num_containers} containers to {destination}",
#         }

#     # -----------------------------------------------------------------------------------------------
#     # -----------------------------------------------------------------------------------------------
#     # SCENARIO 2: This is the first time this tool is called. Large orders need human approval - PAUSE here.
#     if not tool_context.tool_confirmation:
#         tool_context.request_confirmation(
#             hint=f"⚠️ Large order: {num_containers} containers to {destination}. Do you want to approve?",
#             payload={"num_contain ers": num_containers, "destination": destination},
#         )
#         return {  # This is sent to the Agent
#             "status": "pending",
#             "message": f"Order for {num_containers} containers requires approval",
#         }

#     # -----------------------------------------------------------------------------------------------
#     # -----------------------------------------------------------------------------------------------
#     # SCENARIO 3: The tool is called AGAIN and is now resuming. Handle approval response - RESUME here.
#     if tool_context.tool_confirmation.confirmed:
#         return {
#             "status": "approved",
#             "order_id": f"ORD-{num_containers}-HUMAN",
#             "num_containers": num_containers,
#             "destination": destination,
#             "message": f"Order approved: {num_containers} containers to {destination}",
#         }
#     else:
#         return {
#             "status": "rejected",
#             "message": f"Order rejected: {num_containers} containers to {destination}",
#         }


# print("✅ Long-running functions created!")
