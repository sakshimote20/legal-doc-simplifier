import streamlit as st
from simplify import simplify_clause, summarize_text
from qa_engine import build_qa_chain, answer_clause_question


from parser import (
    extract_text_from_pdf,
    extract_text_from_docx,
    extract_text_from_image,
    split_into_clauses,
    get_full_text,
)
from qa_engine import build_qa_chain, answer_clause_question  # ✅ updated import

st.set_page_config(page_title="Legal Clause Simplifier", layout="centered")
st.title("📜 Legal Clause Simplifier")
st.markdown("Upload a legal document (PDF / DOCX / image) or paste a clause below for explanation.")

# ---- Clause Pasting Section ----
st.header("🔍 Paste a Legal Clause")
clause = st.text_area("Clause:", height=150)

if st.button("Simplify Pasted Clause"):
    if clause.strip():
        with st.spinner("Simplifying..."):
            result = simplify_clause(clause)
        st.success("✅ Simplified Explanation:")
        st.write(result)

        st.info("ℹ️ If you want to ask follow-up questions, please upload a full document instead.")

    else:
        st.warning("⚠️ Please enter a clause.")


# ---- File Upload Section ----
st.header("📂 Upload Legal Document (PDF / DOCX / Image)")
uploaded_file = st.file_uploader("Upload a document or a photo of a legal clause", type=["pdf", "docx", "jpg", "jpeg", "png"])

if uploaded_file:
    full_text = get_full_text(uploaded_file)

    if full_text:
        st.success("✅ Text extracted successfully!")

        

        # --- Processing Mode ---
        mode = st.radio("Choose how you want to process the content:",
                        ["🧠 Full Document Summary", "✂️ Clause-by-Clause Simplification"])

        if mode == "🧠 Full Document Summary":
            if st.button("Summarize Document"):
                with st.spinner("Summarizing..."):
                    summary = summarize_text(full_text)
                st.subheader("📝 Summary:")
                st.write(summary)

        elif mode == "✂️ Clause-by-Clause Simplification":
            clauses = split_into_clauses(full_text)
            st.write(f"📑 Found `{len(clauses)}` possible clauses.")
            for i, clause in enumerate(clauses):
                with st.expander(f"Clause {i+1}"):
                    st.write(clause)
                    if st.button(f"Simplify Clause {i+1}", key=f"simp_{i}"):
                        with st.spinner("Simplifying..."):
                            simplified = simplify_clause(clause)
                        st.write("✅ Simplified:")
                        st.write(simplified)

        # --- Q&A Section ---
        st.markdown("---")
        st.header("💬 Ask Questions About This Document")

        qa_chain = build_qa_chain(full_text)
        query = st.text_input("Ask your question here:")

        if query:
            with st.spinner("Thinking..."):
                answer = qa_chain.run(query)
            st.success("✅ Answer:")
            st.write(answer)
   
    else:
      st.error("❌ Could not extract text from the file. Make sure it's not corrupt or blurry.")

