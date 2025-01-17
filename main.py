from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import autogen
from dotenv import load_dotenv
import os

def get_config(provider="openai"):
    """Get configuration based on the chosen provider."""
    if provider == "openai":
        return [{
            "model": "gpt-3.5-turbo",
            "api_key": os.getenv("OPENAI_API_KEY")
        }]
    elif provider == "gemini":
        return [{
            "model": "gemini-pro",
            "api_key": os.getenv("GOOGLE_API_KEY"),
            "api_type": "google"
        }]
    else:
        raise ValueError(f"Unsupported provider: {provider}")

def create_agents(provider="openai"):
    """Create assistant and user proxy agents with specified configuration."""
    # Load environment variables
    load_dotenv()
    
    # Get provider-specific configuration
    config_list = get_config(provider)

    # Settings for code execution
    code_execution_config = {
        "work_dir": "coding",
        "use_docker": False
    }

    # Create an AI assistant agent
    assistant = AssistantAgent(
        name="assistant",
        llm_config={
            "config_list": config_list,
            "seed": 42
        },
        code_execution_config=code_execution_config
    )
    
    # Create a user proxy agent
    user_proxy = UserProxyAgent(
        name="user",
        human_input_mode="NEVER",  # No human input needed
        max_consecutive_auto_reply=3,
        code_execution_config=code_execution_config
    )

    return assistant, user_proxy

def main():
    # Choose the provider (can be modified based on user input or environment variable)
    provider = os.getenv("LLM_PROVIDER", "gemini")  # Default to Gemini if not specified
    
    # Create agents with the chosen provider
    assistant, user_proxy = create_agents(provider)

    # Start a task-oriented conversation
    user_proxy.initiate_chat(
        assistant,
        message="Sort the array with Bubble Sort: [8, 1, 5, 2, 3, 21, 13, 10, 15, 17, 12, 11, 14, 16, 18, 19, 20]"
    )

if __name__ == "__main__":
    main()
