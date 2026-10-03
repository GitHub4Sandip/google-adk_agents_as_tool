from google.adk.agents.llm_agent import LlmAgent, Agent
from google.adk.tools.agent_tool import AgentTool

# Define the specialized worker agent that will be used as a tool.
greeting_expert = LlmAgent(
    name='greeting_expert_agent',
    model='gemini-3.5-flash',
    description='This agent is an expert at creating personalized greetings in different languages.',
    instruction="""You are a greeting expert. A user will provide a name and a language.
    Create a friendly, personalized greeting. For example: Hola, Maria!""",
)

# Define the main manager agent that will use the worker.
root_agent = Agent(
    name='delegator_agent',
    model='gemini-3.5-flash',
    instruction="""You are a helpful assistant. If the user asks for any kind of greeting,
    delegate the task to the `greeting_expert_agent` tool. Forward the user's
    request exactly as you receive it.""",

    # Wrap the worker agent in AgentTool and provide it as a tool to the manager.
    tools=[AgentTool(agent=greeting_expert)]
)