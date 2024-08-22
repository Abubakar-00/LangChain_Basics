import os
from dotenv import load_dotenv

from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

# Load environment variables from .env
load_dotenv()

# Define the directory containing the text file and the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "odyssey.txt")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Check if the Chroma vector store already exists
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Ensure the text file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Read the text content from the file
    loader = TextLoader(file_path , encoding='utf-8')
    documents = loader.load()

    # Split the document into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings
    print("\n--- Creating embeddings ---")
    # embeddings = OpenAIEmbeddings(
    #     model="text-embedding-3-small"
    # )  # Update to a valid embedding model if needed

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    ) 

    print("\n--- Finished creating embeddings ---")

    # Create the vector store and persist it automatically
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs, embeddings, persist_directory=persistent_directory)
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")


# import os
# from dotenv import load_dotenv

# from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.document_loaders import TextLoader
# from langchain_community.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings

# # Load environment variables from .env
# load_dotenv()

# # Define the directory containing the text file and the persistent directory
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, "books", "odyssey.txt")
# persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# # Check if the Chroma vector store already exists
# if not os.path.exists(persistent_directory):
#     print("Persistent directory does not exist. Initializing vector store...")

#     # Ensure the text file exists
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(
#             f"The file {file_path} does not exist. Please check the path."
#         )

#     # Read the text content from the file
#     loader = TextLoader(file_path, encoding='utf-8')
#     documents = loader.load()

#     # Split the document into chunks
#     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
#     docs = text_splitter.split_documents(documents)

#     # Display information about the split documents
#     print("\n--- Document Chunks Information ---")
#     print(f"Number of document chunks: {len(docs)}")
#     print(f"Sample chunk:\n{docs[0].page_content}\n")

#     # Create embeddings
#     print("\n--- Creating embeddings ---")
#     embeddings = GoogleGenerativeAIEmbeddings(
#         model="models/embedding-001"
#     )

#     # Batch process the document chunks to avoid exceeding the request limit
#     batch_size = 100
#     all_embeddings = []
#     for i in range(0, len(docs), batch_size):
#         batch_docs = docs[i:i + batch_size]
#         batch_embeddings = embeddings.embed_documents([doc.page_content for doc in batch_docs])
#         all_embeddings.extend(batch_embeddings)

#     print("\n--- Finished creating embeddings ---")

#     # Create the vector store and persist it automatically
#     print("\n--- Creating vector store ---")
#     db = Chroma(docs, embeddings, persist_directory=persistent_directory)
#     db.persist()
#     print("\n--- Finished creating vector store ---")

# else:
#     print("Vector store already exists. No need to initialize.")
