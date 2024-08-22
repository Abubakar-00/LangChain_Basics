from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# Load the text file
loader = TextLoader("cloud.txt")

documents = loader.load()

# Split documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Create embeddings using GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Create a ChromaDB vector store
vectorstore = Chroma(embedding_function=embeddings, collection_name="testing_db")
vectorstore.add_documents(docs)

# Use the retriever to find relevant documents
query = "What is title of txt file"
docs = vectorstore.similarity_search(query)

# Process the retrieved documents
for doc in docs:
    print(doc.page_content)
