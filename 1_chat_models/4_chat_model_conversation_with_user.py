from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables from .env
load_dotenv()

# Create a ChatGroq model
model = ChatGroq(model_name="mixtral-8x7b-32768")


chat_history = []  # Use a list to store messages

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI Digital Marketer.")
chat_history.append(system_message)  # Add system message to chat history

# Chat loop
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query))  # Add user message

    # Get AI response using history
    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response))  # Add AI message

    print(f"AI: {response}")


print("---- Message History ----")
print(chat_history)
