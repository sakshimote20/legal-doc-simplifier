# 📜 Legal Clause Simplifier

An AI-powered web application that simplifies complex legal documents, provides clause-wise explanations, summarizes full documents, and answers user queries — helping users understand legal language with ease.

Built using Streamlit, LangChain, Cohere LLM, and OCR tools.

---

## 🚀 Features

- 🔍 **Paste Clause Simplifier**: Paste any legal clause and get a plain-language explanation.
- 📂 **Document Upload**: Upload PDF, DOCX, or image files of legal documents.
- ✂️ **Clause-by-Clause Simplification**: Breaks document into clauses and explains each in plain English.
- 🧠 **Full Document Summary**: Summarizes entire legal documents in simple language.
- 💬 **Q&A Chatbot**: Ask questions related to the uploaded document using RAG (Retrieval-Augmented Generation).
- 📸 **OCR Support**: Extracts text from scanned images or photos of legal clauses.
- ⚠️ **Error Handling**: Graceful error messages for corrupt files or unreadable documents.

---

## 🧠 Tech Stack

| Tool/Library      | Purpose |
|-------------------|---------|
| `Streamlit`       | UI and frontend |
| `LangChain`       | LLM orchestration and RAG |
| `Cohere (command-r-plus)` | Large Language Model |
| `FAISS`           | Vector search for Q&A |
| `PyMuPDF`         | PDF text extraction |
| `python-docx`     | DOCX file handling |
| `Pytesseract`     | OCR for images |
| `dotenv`          | Environment variable management |

---

## 📁 Folder Structure

```
legal-simplifier-app/
│
├── app.py                    # Main Streamlit app
├── simplify.py               # Clause simplifier & summarizer functions
├── parser.py                 # PDF, DOCX, Image text extraction
├── qa_engine.py              # Q&A system with RAG and prompt-based answer
├── requirements.txt
├── .env                      # API key for Cohere
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/sakshimote20/legal-simplifier-app.git
   cd legal-simplifier-app
   ```

2. **Create virtual environment and activate**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root folder:

   ```env
   COHERE_API_KEY=your_actual_cohere_api_key
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🔐 API Key

- Sign up at [Cohere](https://cohere.com/) and get a free API key.
- Add it to your `.env` file as shown above.

---

## 🧪 Sample Use Cases

| Use Case | What You Can Do |
|----------|------------------|
| 📃 Rental Agreement | Understand tricky clauses before signing |
| 🧾 Offer Letters     | Check for non-compete or notice period clauses |
| 🔒 Privacy Policies | Summarize what data is collected and shared |
| 📑 Government Forms | Simplify certificate contents for better understanding |

---

## 👩‍💻 Author

**Sakshi Mote**  
3rd Year AI & Data Science Student  
GitHub: [@sakshimote](https://github.com/sakshimote20)

---

## 📌 Future Ideas

- 🧠 Built-in Legal Glossary for term definitions
- 📥 Export summary as PDF
- 📱 Mobile-responsive design

---

