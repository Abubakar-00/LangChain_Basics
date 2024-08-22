from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a GroqAI model
model = ChatGroq(model_name="mixtral-8x7b-32768")

# SystemMessage:
#   Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse:
#   Message from a human to the AI model.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")


# AIMessage:
#   Message from an AI.
messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="Sure, I can help with that! The result of dividing 81 by 9 is 9. Explanation: When you divide a number by another number, you are finding out how many times the second number can go into the first number. In this case, you want to know how many times 9 can go into 81. The answer is 9 times because: 9 x 9 = 81So, 81 divided by 9 is equal to 9."),
    HumanMessage(content="What is 10 times 5?"),
]

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
