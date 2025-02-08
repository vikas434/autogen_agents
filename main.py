from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="AutoGen Chat API")

# Basic configuration for Gemini
config_list = [{
    "model": "gemini-pro",
    "api_key": os.getenv("GOOGLE_API_KEY"),
    "api_type": "google"
}]

# Configure code execution settings
code_execution_config = {
    "work_dir": "coding",  # Directory for code execution
    "use_docker": False    # Don't use Docker
}

# Create an AI assistant agent
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
    code_execution_config=code_execution_config,
    max_consecutive_auto_reply=1  # This ensures only one response
)

# Create a user proxy agent
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config=code_execution_config
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    # Start a conversation with the provided message
    chat_response = user_proxy.initiate_chat(
        assistant,
        message=request.message
    )
    
    # Extract the last message from the conversation
    last_message = chat_response[-1]['content'] if chat_response else "No response"
    return {"response": last_message}

@app.get("/")
async def root():
    return {"message": "Welcome to AutoGen Chat API"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
