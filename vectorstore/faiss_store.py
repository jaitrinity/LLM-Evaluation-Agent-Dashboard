import faiss
import numpy as np

index = None
texts = []

def create_index(embeddings, chunks):
    global index, texts

    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings).astype("float32"))
    texts = chunks


def search(query_embedding, k=3):
    global index, texts

    if index is None:
        raise ValueError("FAISS index not created. Upload PDF first.")

    distances, indices = index.search(query_embedding, k)

    return [texts[i] for i in indices[0]]