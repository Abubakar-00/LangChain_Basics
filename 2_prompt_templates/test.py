from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

print("-----Prompt from Template-----")
template = "Tell me a joke about {topic}."
# create template
prompt_template = ChatPromptTemplate.from_template(template)

# invoke template
prompt = prompt_template.invoke({"topic":"cat"})
# invoke model
result = model.invoke(prompt)
print(result.content)


messages = [
    ("system", "You are a comedian who tells jokes about {topic}."),
    ("human", "Tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})
result = model.invoke(prompt)
print(result.content)