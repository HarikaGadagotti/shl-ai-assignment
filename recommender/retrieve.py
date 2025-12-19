import pickle
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def load_embeddings():
    with open("embeddings/embeddings.pkl", "rb") as f:
        data = pickle.load(f)
    return data["embeddings"], pd.DataFrame(data["data"])

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, top_k=5):
    embeddings, df = load_embeddings()
    query_vec = model.encode([query])
    scores = cosine_similarity(query_vec, embeddings)[0]

    df["score"] = scores
    results = df.sort_values("score", ascending=False).head(top_k)

    return results[["name", "url"]]

if __name__ == "__main__":
    q = "Hiring a Java developer with good collaboration skills"
    print(retrieve(q))

