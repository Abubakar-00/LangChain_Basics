from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

chat_history = []

system_message = SystemMessage(content="You are professional Photographer")
chat_history.append(system_message)

while True:
    qurey = input("You: ")
    if qurey.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=qurey))

    result = model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(response))

    print(f"AI: {response}")

print("---- Message History ----")
print(chat_history)
