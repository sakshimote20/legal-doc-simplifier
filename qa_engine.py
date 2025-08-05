import os
from dotenv import load_dotenv
from langchain_community.llms import Cohere
from langchain_community.embeddings import CohereEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document

# Load .env
load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")

# ✅ Shared LLM
llm = Cohere(
    cohere_api_key=cohere_api_key,
    model="command-r-plus",
    temperature=0.3,
    max_tokens=300
)

# ✅ For PDF/DOCX/Image documents
def build_qa_chain(text):
    doc = Document(page_content=text)

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.split_documents([doc])

    # Create embeddings and vector store
    embeddings = CohereEmbeddings(
        cohere_api_key=cohere_api_key,
        model="embed-english-v3.0",  # or embed-multilingual-v3.0
        user_agent="legal-simplifier-app"
    )
    vectordb = FAISS.from_documents(docs, embeddings)
    retriever = vectordb.as_retriever()

    # Create Retrieval-based QA chain
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
    return qa_chain

# ✅ For single clause + question (direct prompt)
def answer_clause_question(clause, question):
    prompt = f"""
You are a helpful legal assistant. Below is a legal clause and a user's question.
Answer clearly and accurately based only on the clause.

Clause:
\"\"\"
{clause}
\"\"\"

Question: {question}

Answer:
"""
    return llm.invoke(prompt)
