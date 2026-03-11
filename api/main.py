from fastapi import FastAPI, UploadFile
from rag.pdf_loader import load_pdf
from rag.chunker import chunk_text
from vectorstore.faiss_store import create_index
from rag.retriever import retrieve
from llm.generator import generate_answer
from rag.embeddings import embed_chunks
from metrics.similarity import similarity
from metrics.bleu import bleu
from metrics.rouge import rouge
from metrics.hallucination import detect

app = FastAPI()

@app.post("/upload_pdf")
async def upload(file: UploadFile):

    text = await load_pdf(file)

    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)

    create_index(embeddings, chunks)

    return {"message": "PDF processed"} 


@app.get("/ask")
def ask(question: str):

    context = retrieve(question)

    answer = generate_answer(question, context)

    reference = " ".join(context)

    sim = similarity(reference, answer)

    bleu_score = bleu(reference, answer)

    rouge_score = rouge(reference, answer)

    hallucination = sim < 0.4

    return {
        "answer": answer,
        "similarity": sim,
        "bleu": bleu_score,
        "rouge": rouge_score,
        "hallucination": hallucination
    }