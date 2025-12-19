import pandas as pd
from recommender.retrieve import retrieve

test_queries = [
    "Hiring a Java backend developer",
    "Looking for leadership assessment",
    "Need cognitive ability test",
    "Software testing skills required"
]

def evaluate():
    for q in test_queries:
        results = retrieve(q, top_k=3)
        print(f"\nQuery: {q}")
        for _, row in results.iterrows():
            print("-", row["name"])

if __name__ == "__main__":
    evaluate()
