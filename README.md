# SecureGov RAG Pipeline

## Project Overview
A compliance-focused Retrieval-Augmented Generation (RAG) pipeline designed for **GovCloud** and **FinTech** environments. This system enables secure document querying while strictly enforcing **Data Sovereignty** and **PII Protection**.

Unlike standard RAG implementations, this architecture creates a "air gap" between sensitive internal data and public LLMs, ensuring no confidential information is used for model training.

## Architecture
* **Ingestion Engine:** Python + LangChain for PDF parsing and recursive chunking.
* **Vector Store:** Pinecone (Isolated Index) for semantic search.
* **Security Layer:** Automated PII (Personally Identifiable Information) redaction before embedding.
* **Infrastructure:** Dockerized microservices deployable to AWS ECS (Fargate).

## Tech Stack
* **Language:** Python 3.10+
* **AI Framework:** LangChain
* **Database:** Pinecone (Vector DB)
* **DevOps:** Docker, GitHub Actions

## Getting Started

### Prerequisites
* Python 3.10+
* Docker Desktop
* API Keys (Pinecone, Google Gemini/OpenAI)

### Installation
1. **Clone the repository**
   ```powershell
   git clone [https://github.com/jt96/secure-rag-pipeline.git](https://github.com/jt96/secure-rag-pipeline.git)
   cd secure-rag-pipeline
   ```

2. **Set up the environment (Windows)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configuration**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   PINECONE_API_KEY=your_key_here
   GOOGLE_API_KEY=your_key_here
   PINECONE_INDEX_NAME=your_index_here
   ```

## Docker Support
Run the application in an isolated container:

1. Build the image:
   `docker build -t rag-app .`

2. Run the chat (injects API keys automatically):
   `docker run -it --env-file .env rag-app`