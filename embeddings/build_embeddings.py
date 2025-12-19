import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
import os

def main():
    print("Loading data...")
    df = pd.read_csv("data/shl_assessments.csv")

    # Combine available text fields (only name for now)
    texts = df["name"].fillna("").tolist()

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Creating embeddings...")
    embeddings = model.encode(texts, show_progress_bar=True)

    os.makedirs("embeddings", exist_ok=True)

    with open("embeddings/embeddings.pkl", "wb") as f:
        pickle.dump({
            "embeddings": embeddings,
            "data": df
        }, f)

    print("Embeddings saved successfully!")

if __name__ == "__main__":
    main()
