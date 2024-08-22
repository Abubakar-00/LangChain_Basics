import os
from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

# Load environment variables from .env
load_dotenv()

# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Define the embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Function to convert proto repeated fields to lists
def convert_embedding_to_list(embedding):
    return list(embedding)

# Load the existing vector store with the embedding function
db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)

# Define the user's question
query = "Who is Odysseus' wife?"

# Retrieve relevant documents based on the query
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 3, "score_threshold": 0.5},
)

try:
    relevant_docs = retriever.invoke(query)
except ValueError as e:
    print(f"Error during retrieval: {e}")
    # Debugging: Check the format of the embeddings
    sample_embedding = embeddings.embed_query(query)
    converted_embedding = convert_embedding_to_list(sample_embedding)
    print(f"Sample embedding: {converted_embedding}")
    print(f"Type of converted embedding: {type(converted_embedding)}")
    if isinstance(converted_embedding, list) and all(isinstance(i, float) for i in converted_embedding):
        print("Embeddings are in the correct format.")
    else:
        print("Embeddings are not in the correct format.")

# If retrieval was successful, display the relevant results with metadata
if 'relevant_docs' in locals():
    print("\n--- Relevant Documents ---")
    for i, doc in enumerate(relevant_docs, 1):
        print(f"Document {i}:\n{doc.page_content}\n")
        if doc.metadata:
            print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")
else:
    print("No relevant documents found.")
