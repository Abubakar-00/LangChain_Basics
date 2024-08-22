# LangChain Basics

This whole code base is adopted from "codewithbrandon". I have used OpenAI Free alternatives such as GoogleGenAI and Groq Api's.
I have adopted GoogleGenAI Embedder-01, Gemnini Flash 1.5 (LLM) and Groq Mistral 8x7B (LLM).

## Course Outline

1. **Setup Environment**
2. **Chat Models**
3. **Prompt Templates**
4. **Chains**
5. **RAG (Retrieval-Augmented Generation)**
6. **Agents & Tools**

## Getting Started

### Prerequisites

- Python 3.10 or 3.11
- Poetry (Follow this [Poetry installation tutorial](https://python-poetry.org/docs/#installation) to install Poetry on your system)

### Installation

1. Clone the repository:

   Brandon's Repository

   ```bash
   <!-- TODO: UPDATE TO MY  -->
   git clone https://github.com/bhancockio/langchain-crash-course
   cd langchain-crash-course
   ```
   My Repository:

   ```bash
   https://github.com/Abubakar-00/LangChain_Basics.git
   ```

3. Install dependencies using Poetry or Requirements file:

   ```bash
   poetry install --no-root
   ```

   If you want to install dependencies from requirement file.
   
   ```bash
   pip install -r requirements. txt
   ```

4. Set up your environment variables:

   - Just open .env files and paste your API keys without quotation.

   ```bash
   TAVILY_API_KEY=ADD_KEY_HERE
   TAVILY_API_KEY=Example1234
   ```

   

5. Activate the Poetry shell to run the examples (Depends upon your preference):

   ```bash
   poetry shell
   ```

6. Run the code examples:

   ```bash
    python chat_models/1_chat_model_basic.py
   ```

## Repository Structure

Here's a breakdown of the folders and what you'll find in each:

### 1. Chat Models

- `1_chat_model_basic.py`
- `2_chat_model_basic_conversation.py`
- `3_chat_model_alternatives.py`
- `4_chat_model_conversation_with_user.py`
- `5_chat_model_save_message_history_firestore.py`

Learn how to interact with models like ChatGPT, Claude, and Gemini.

### 2. Prompt Templates

- `1_prompt_template_basic.py`
- `2_prompt_template_with_chat_model.py`

Understand the basics of prompt templates and how to use them effectively.

### 3. Chains

- `1_chains_basics.py`
- `2_chains_under_the_hood.py`
- `3_chains_extended.py`
- `4_chains_parallel.py`
- `5_chains_branching.py`

Learn how to create chains using Chat Models and Prompts to automate tasks.

### 4. RAG (Retrieval-Augmented Generation)

- `1a_rag_basics.py`
- `1b_rag_basics.py`
- `2a_rag_basics_metadata.py`
- `2b_rag_basics_metadata.py`
- `3_rag_text_splitting_deep_dive.py`
- `4_rag_embedding_deep_dive.py`
- `5_rag_retriever_deep_dive.py`
- `6_rag_one_off_question.py`
- `7_rag_conversational.py`
- `8_rag_web_scrape_firecrawl.py`
- `8_rag_web_scrape.py`

Explore the technologies like documents, embeddings, and vector stores that enable RAG queries.

### 5. Agents & Tools

- `1_agent_and_tools_basics.py`
- `agent_deep_dive/`
  - `1_agent_react_chat.py`
  - `2_react_docstore.py`
- `tools_deep_dive/`
  - `1_tool_constructor.py`
  - `2_tool_decorator.py`
  - `3_tool_base_tool.py`

## License

This project is licensed under the MIT License.
