from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time():
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {"Current time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that uses tools to answer the user's question:
    - google search
    - get current time
    """,
    tools=[get_current_time] # google_search
)