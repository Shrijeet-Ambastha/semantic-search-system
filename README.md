# Semantic Search System with Semantic Cache

## Overview

This project implements a **lightweight semantic search system** built on the **20 Newsgroups dataset**.
The system uses **vector embeddings**, **fuzzy clustering**, and a **semantic cache** to efficiently retrieve relevant information from text data.

Unlike traditional keyword search, this system understands **semantic meaning**, allowing it to recognize similar queries even when phrased differently.

The project also exposes the functionality through a **FastAPI REST API**, making it easy to interact with the system programmatically.

---

# Dataset

Dataset used: **20 Newsgroups Dataset**

Source:
https://archive.ics.uci.edu/dataset/113/twenty+newsgroups

The dataset contains approximately **20,000 news articles** categorized into **20 different topics**, including:

* Technology
* Space
* Politics
* Sports
* Religion
* Computer hardware/software

To reduce noise and improve embedding quality, the following elements were removed:

* Email headers
* Message footers
* Quoted replies

---

# System Architecture

The system pipeline works as follows:

1. Load dataset
2. Generate embeddings using Sentence Transformers
3. Store embeddings in a FAISS vector database
4. Perform fuzzy clustering on document embeddings
5. Use semantic cache to reuse similar query results
6. Expose functionality via FastAPI endpoints

This design ensures **efficient semantic search and reduced redundant computation**.

---

# Key Components

## 1. Embedding Generation

Text documents and queries are converted into numerical vectors using the model:

```
sentence-transformers/all-MiniLM-L6-v2
```

Reasons for selecting this model:

* Lightweight
* Fast inference
* Good semantic understanding

---

## 2. Vector Database (FAISS)

FAISS is used to store embeddings and perform efficient similarity searches.

Benefits:

* Fast vector similarity search
* Scales well for large datasets
* Efficient memory usage

---

## 3. Fuzzy Clustering

Unlike traditional clustering where a document belongs to one cluster, fuzzy clustering allows documents to belong to **multiple clusters with probabilities**.

Example:

```
Document X
Cluster 1: 0.60
Cluster 2: 0.30
Cluster 3: 0.10
```

This approach better represents documents that contain **multiple topics**.

---

## 4. Semantic Cache

Traditional caching only works when queries are identical.

Example:

```
Query 1: "space exploration"
Query 2: "space exploration"
```

However, users may phrase the same question differently:

```
Query 1: "space exploration missions"
Query 2: "NASA mission discussion"
```

Semantic cache solves this problem by:

1. Converting queries to embeddings
2. Measuring cosine similarity
3. Reusing cached results if similarity exceeds a threshold

This reduces computation and improves response time.

---

# API Implementation

The system exposes functionality through a **FastAPI server**.

API documentation is automatically generated using **Swagger UI**.

### Start the server

```
python -m uvicorn api.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## POST /query

Accepts a natural language query.

### Request

```
{
  "query": "space exploration missions"
}
```

### Response

```
{
  "query": "...",
  "cache_hit": true,
  "matched_query": "...",
  "similarity_score": 0.91,
  "result": "...",
  "dominant_cluster": 3
}
```

If the query is similar to a previous query, the system returns a **cache hit**.

---

## GET /cache/stats

Returns statistics about the semantic cache.

Example response:

```
{
 "total_entries": 3,
 "hit_count": 1,
 "miss_count": 2,
 "hit_rate": 0.33
}
```

---

## DELETE /cache

Clears all entries in the semantic cache and resets statistics.

Example response:

```
{
 "message": "Cache cleared"
}
```

---

# Project Structure

```
semantic-search-system
│
├── api
│   └── main.py
│
├── cache
│   └── semantic_cache.py
│
├── clustering
│   └── fuzzy_cluster.py
│
├── data
│   └── dataset_loader.py
│
├── embeddings
│   └── embedder.py
│
├── vector_db
│   └── faiss_store.py
│
├── test_pipeline.py
├── test_cache.py
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone <your-repo-link>
cd semantic-search-system
```

Create virtual environment:

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Running the System

Run the FastAPI server:

```
python -m uvicorn api.main:app --reload
```

Open API interface:

```
http://127.0.0.1:8000/docs
```

---

# Technologies Used

* Python
* FastAPI
* Sentence Transformers
* FAISS
* Scikit-learn
* NumPy
* Scikit-fuzzy
* Uvicorn

---

# Author

Shrijeet Ambastha
