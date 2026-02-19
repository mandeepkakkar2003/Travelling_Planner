from google.adk.agents import LlmAgent

activity_agent = LlmAgent(
    name="activity_agent",
    model="gemini-2.0-flash-lite",
    instruction="""
You are an activity planning specialist.

Your job:
- Suggest top 3 activities for the destination.
- Organize by day if possible.
- Keep output structured.
"""
)
