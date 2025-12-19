from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from recommender.retrieve import retrieve

app = FastAPI()

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all (OK for assignment)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend(req: QueryRequest):
    results = retrieve(req.query, top_k=10)

    output = []
    for _, row in results.iterrows():
        output.append({
# Note: adaptive_support, remote_support, test_type are inferred defaults
# because public catalog does not expose structured metadata

            "name": row["name"],
            "url": row["url"],
            "adaptive_support": "Yes",
            "description": row["name"],
            "duration": 30,
            "remote_support": "Yes",
            "test_type": ["Knowledge & Skills"]
        })

    return {"recommended_assessments": output}
