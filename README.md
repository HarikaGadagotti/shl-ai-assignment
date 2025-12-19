# SHL Assessment Recommendation Engine  
**Research Intern – Generative AI Assignment (SHL)**

---

## 1. Project Overview

This project implements an **Assessment Recommendation Engine** using SHL’s public product catalog.  
Given a job description or hiring requirement, the system recommends the most relevant SHL assessments using **semantic similarity with sentence embeddings**.

The solution follows a **retrieval-based Generative AI approach**, combining:
- Data collection from SHL product catalog
- Embedding-based semantic search
- FastAPI backend service
- Streamlit UI
- Offline evaluation using a provided dataset

---

## 2. Architecture

User Query
↓
Sentence Embedding (MiniLM)
↓
Cosine Similarity Search
↓
Top-K Relevant SHL Assessments
↓
FastAPI Response
↓
Streamlit UI

---

## 3. Tech Stack

- **Python 3.12**
- **Sentence Transformers** (`all-MiniLM-L6-v2`)
- **FastAPI** – Backend API
- **Streamlit** – UI
- **Pandas / NumPy**
- **scikit-learn**
- **Requests**

---


## 4. Folder Structure

```text
shl-ai-assignment/
│
├── data/
│   ├── shl_assessments.csv        # Scraped SHL assessment catalogue
│   └── Gen_AI Dataset.xlsx        # Provided evaluation dataset
│
├── scraper/
│   └── scrape_shl.py              # SHL product catalog scraper
│
├── embeddings/
│   ├── build_embeddings.py        # Sentence embedding generation
│   └── embeddings.pkl             # Saved embeddings and metadata
│
├── recommender/
│   └── retrieve.py                # Semantic retrieval logic
│
├── api/
│   └── main.py                    # FastAPI backend
│
├── ui/
│   └── app.py                     # Streamlit frontend
│
├── evaluation/
│   ├── basic_eval.py              # Sanity evaluation
│   └── generate_submission.py     # Generates final submission CSV
│
├── requirements.txt
└── README.md


---

## 5. Data Sources

### 5.1 SHL Product Catalog

Assessments were collected from:  
https://www.shl.com/products/product-catalog/

Stored as:
data/shl_assessments.csv


---

### 5.2 Provided Evaluation Dataset

The file **`Gen_AI Dataset.xlsx`** (provided as part of the assignment) is used **only for evaluation and submission generation**, not for model training.

Location:
data/Gen_AI Dataset.xlsx


---

## 6. Setup Instructions

### 6.1 Create Virtual Environment

python -m venv venv
source venv/bin/activate
6.2 Install Dependencies

pip install -r requirements.txt

## 7. Running the Project (Local)
### 7.1 Scrape SHL Catalog

python scraper/scrape_shl.py
Output:

data/shl_assessments.csv

### 7.2 Generate Embeddings

python embeddings/build_embeddings.py
Output:

embeddings/embeddings.pkl

### 7.3 Start FastAPI Backend

uvicorn api.main:app --reload
Swagger UI:
http://127.0.0.1:8000/docs

### 7.4 Run Streamlit UI

streamlit run ui/app.py
UI URL:

http://localhost:8501
### 8. API Endpoints
Health Check

GET /health
Recommend Assessments

POST /recommend
Request Body


{
  "query": "Hiring a Java backend developer"
}
Response

json
{
  "recommended_assessments": [
    {
      "name": "Java Platform Enterprise Edition",
      "url": "https://www.shl.com/...",
      "adaptive_support": "Yes",
      "remote_support": "Yes",
      "duration": 30,
      "test_type": ["Knowledge & Skills"]
    }
  ]
}
## 8. Evaluation
### 8.1 Run Basic Evaluation

PYTHONPATH=. python evaluation/basic_eval.py
This prints top recommendations for sample queries.

8.2 Final Submission CSV
PYTHONPATH=. python evaluation/generate_submission.py
Output:

submission.csv
This file is generated using Gen_AI Dataset.xlsx as required by the assignment.


10. Final Submission Checklist
GitHub repository (complete project)

README.md

submission.csv

Evaluation scripts

Working API and UI locally

13. Author
Harika Gadagotti
