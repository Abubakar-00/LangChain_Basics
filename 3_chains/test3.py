from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain.prompts import ChatPromptTemplate


load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)

lower_case = RunnableLambda(lambda x: x.lower())
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

chain = prompt_template | model | StrOutputParser() | lower_case | count_words

result = chain.invoke({"topic": "lawyers", "joke_count": 3})

print(result)