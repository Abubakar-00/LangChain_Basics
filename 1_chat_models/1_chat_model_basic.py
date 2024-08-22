# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# GroqAI Chat Model Documents: https://api.python.langchain.com/en/latest/chat_models/langchain_groq.chat_models.ChatGroq.html

from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a ChatGroq model
model = ChatGroq(model_name="mixtral-8x7b-32768")

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
 