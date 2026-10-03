# Agents as Tool

A Python project demonstrating how to use **Google ADK (Agent Development Kit)** to create a manager-worker agent architecture where specialized worker agents can be wrapped as tools for a main agent.

## Project Overview

This project showcases a delegation pattern where:
- A **manager agent** (`delegator_agent`) handles user requests and routes tasks
- A **worker agent** (`greeting_expert_agent`) specializes in creating personalized greetings in different languages
- The worker agent is wrapped as an `AgentTool` and made available to the manager agent

This pattern enables building complex, multi-agent systems where agents can delegate work to specialized sub-agents.

## Requirements

- Python 3.13 or higher
- Google ADK 2.9.2 or higher
- Google API key for Gemini access

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agents_as_tool
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or using UV
   uv sync
   ```

4. Set up environment variables:
   - Create or update a `.env` file with your Google API credentials:
     ```env
     GOOGLE_API_KEY=your_api_key_here
     GOOGLE_GENAI_USE_ENTERPRISE=0
     ```

## Project Structure

```
agents_as_tool/
├── agent.py                 # Main agent definitions and configuration
├── pyproject.toml          # Project metadata and dependencies
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore rules
├── .adk/                  # ADK configuration directory
└── README.md              # This file
```

## Usage

### Running the Main Agent

The `agent.py` file defines:

1. **Greeting Expert Agent** (`greeting_expert_agent`)
   - Specialized LLM agent that creates personalized greetings
   - Can handle multiple languages
   - Model: `gemini-3.5-flash`

2. **Delegator Agent** (`root_agent`)
   - Main entry point for the application
   - Routes greeting requests to the greeting expert
   - Model: `gemini-3.5-flash`

To interact with the agents, you can instantiate and call the `root_agent`:

```python
from agent import root_agent

# Example usage
response = root_agent.run("Create a greeting in Spanish for Maria")
print(response)
```

## Architecture

### Manager-Worker Pattern

```
User Input
    ↓
Delegator Agent (root_agent)
    ↓
[Decision: Route to specialized agent]
    ↓
Greeting Expert Agent (greeting_expert_agent)
    ↓
Response
```

This architecture allows:
- **Scalability**: Add more specialized agents as needed
- **Specialization**: Each agent focuses on specific tasks
- **Reusability**: Wrap any agent as a tool for other agents
- **Maintainability**: Easier to update individual agent behaviors

## Key Components

### Agent Definitions

- **LlmAgent**: Specialized worker agents with specific instructions
- **Agent**: Main manager agent with tool capabilities
- **AgentTool**: Wrapper that converts agents into callable tools

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| google-adk | >=2.9.2 | Core Agent Development Kit for building AI agents |

## Configuration

The project uses:
- **Python Version**: 3.13+
- **Package Manager**: UV (or pip)
- **LLM Model**: Gemini 3.5 Flash for fast, efficient responses
- **API**: Google Generative AI API

## Development

### Prerequisites for Development

- Python 3.13+
- UV or pip for package management
- Git for version control

### Running the Project

1. Ensure your `.env` file has a valid `GOOGLE_API_KEY`
2. Run the agent:
   ```bash
   python -m agent
   ```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GOOGLE_API_KEY` | Yes | Your Google API key for Gemini access |
| `GOOGLE_GENAI_USE_ENTERPRISE` | No | Set to 1 for enterprise, 0 for standard (default: 0) |

## Notes

- This project demonstrates the Google ADK agent tool wrapping capability
- The greeting expert agent is a simple example; the pattern can be extended to more complex domains
- Ensure your Google API key is kept secure and not committed to version control

## License

This project is part of the Google ADK learning materials.

## Support

For issues or questions about Google ADK, refer to the [official Google ADK documentation](https://ai.google.dev/adk).
