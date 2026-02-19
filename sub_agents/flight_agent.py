from google.adk.agents import LlmAgent

flight_agent = LlmAgent(
    name="flight_agent",
    model="gemini-2.0-flash-lite",
    instruction="""
You are a flight specialist agent.

Your job:
- Suggest 2 affordable flight options.
- Include airline name and approximate price.
- Keep response short and structured.
"""
)
