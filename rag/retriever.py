from rag.embeddings import embed_chunks
from vectorstore.faiss_store import search

def retrieve(question):

    q_emb = embed_chunks([question])

    chunks = search(q_emb)

    return chunks