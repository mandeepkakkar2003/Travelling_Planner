import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent

from google.adk.tools import google_search



from tools.cost_tool import calculate_total_cost
from sub_agents.flight_agent import flight_agent
from sub_agents.hotel_agent import hotel_agent
from sub_agents.activity_agent import activity_agent


load_dotenv()
# print("API KEY LOADED:", os.getenv("GOOGLE_API_KEY"))
root_agent = LlmAgent(
    name="travel_planner_root",
    model="gemini-2.0-flash-lite",
    instruction="""
You are the root orchestrator of a multi-agent travel planner.

Workflow:
1. Delegate flight-related queries to flight_agent.
2. Delegate hotel-related queries to hotel_agent.
3. Delegate activity planning to activity_agent.
4. Use calculate_total_cost to compute total cost.

Combine all results into a structured travel plan.
""",
    tools=[calculate_total_cost, google_search],
    sub_agents=[flight_agent, hotel_agent, activity_agent]
)
