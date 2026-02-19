from google.adk.agents import LlmAgent

hotel_agent = LlmAgent(
    name="hotel_agent",
    model="gemini-2.0-flash-lite",
    instruction="""
You are a hotel specialist agent.

Your job:
- Suggest 2 hotels within budget.
- Include hotel name and price per night.
- Keep response structured.
"""
)
