import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from environment
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

# Initialize model
model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# Messages
messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

# Invoke model
response = model.invoke(messages)
print(response.content)
