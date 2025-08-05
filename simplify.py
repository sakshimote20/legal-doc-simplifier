e# LLM logic using Cohere
import os
import streamlit as st
import cohere
from dotenv import load_dotenv

#load_dotenv()
#api_key = os.getenv("COHERE_API_KEY") for using with .env file
cohere_api_key = st.secrets["COHERE_API_KEY"]
co = cohere.Client(cohere_api_key)

def simplify_clause(clause_text):
    prompt = f"""You are a legal assistant. Explain the following legal clause in plain, easy-to-understand English:\n\n\"{clause_text}\"\n\nExplanation:"""
    
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=300,
        temperature=0.5,
    )
    
    return response.generations[0].text.strip()

def summarize_text(full_text):
    prompt = f"""You are a legal assistant. Summarize the following legal document in clear, simple English. Highlight what it means, who it is for, and any important takeaways:

Document:
\"\"\"{full_text}\"\"\"

Summary:"""

    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=400,
        temperature=0.5,
    )
    return response.generations[0].text.strip()

