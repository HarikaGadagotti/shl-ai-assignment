import pandas as pd
from recommender.retrieve import retrieve

# Load test queries
df = pd.read_excel("data/Gen_AI Dataset.xlsx")

rows = []

for query in df["Query"]:   
    results = retrieve(query, top_k=10)

    for _, row in results.iterrows():
        rows.append({
            "Query": query,
            "Assessment_url": row["url"]
        })

# Save submission file
submission_df = pd.DataFrame(rows)
submission_df.to_csv("submission.csv", index=False)

print("submission.csv generated successfully!")
