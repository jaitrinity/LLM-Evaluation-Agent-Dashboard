import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="PDF RAG Evaluation")

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Upload PDF", "Ask Question", "Metrics Info"]
)

st.title("PDF Question Answering System")

API = "http://127.0.0.1:8000"


# ========================
# Upload PDF Page
# ========================

if page == "Upload PDF":

    file = st.file_uploader("Upload PDF", type="pdf")

    if file is not None:

        if st.button("Upload"):

            r = requests.post(
                API + "/upload_pdf",
                files={"file": ("file.pdf", file.getvalue())}
            )

            if r.status_code == 200:
                st.success("PDF uploaded and indexed")
            else:
                st.error("Upload failed")


# ========================
# Ask Question Page
# ========================

elif page == "Ask Question":

    question = st.text_input("Ask question from PDF")

    if st.button("Get Answer"):

        r = requests.get(
            API + "/ask",
            params={"question": question}
        )

        if r.status_code == 200:

            data = r.json()

            st.subheader("Answer")
            st.write(data["answer"])

            metrics = {
                "Similarity": data["similarity"],
                "BLEU": data["bleu"],
                "ROUGE": data["rouge"]
            }

            df = pd.DataFrame(metrics.items(), columns=["Metric", "Score"])

            st.subheader("Evaluation Metrics")
            st.table(df)

            if data["hallucination"]:
                st.error("Hallucination Detected")
            else:
                st.success("Answer grounded in PDF")

        else:
            st.error("API error: " + r.text)


# ========================
# Metrics Info Page
# ========================

elif page == "Metrics Info":

    metric = st.selectbox(
        "Select Metric",
        ["Similarity", "BLEU", "ROUGE", "Hallucination"]
    )

    if metric == "Similarity":
        st.write("Semantic similarity between context and answer.")

    elif metric == "BLEU":
        st.write("Measures n-gram overlap between generated answer and reference.")

    elif metric == "ROUGE":
        st.write("Measures recall overlap between generated answer and reference.")

    elif metric == "Hallucination":
        st.write("Detects if the answer contains unsupported information not present in the PDF.")