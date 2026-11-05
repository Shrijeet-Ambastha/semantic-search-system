# Semantic Search System

A semantic search system that uses **vector embeddings** to retrieve relevant results faster. Instead of matching keywords, documents and queries are converted into embeddings and compared by meaning, using a vector index for fast similarity lookup.

## Features

- Embedding-based semantic retrieval (meaning, not just keywords)
- Fast nearest-neighbour search with a FAISS vector index
- Clustering of documents to organise and speed up retrieval
- Caching layer for repeated or similar queries
- REST API built with FastAPI
- Test scripts for the cache and the end-to-end pipeline

## Tech Stack

| Area              | Technology                          |
|-------------------|-------------------------------------|
| Language          | Python                              |
| Embeddings        | sentence-transformers, transformers, PyTorch |
| Vector search     | FAISS (`faiss-cpu`)                 |
| Clustering / ML   | scikit-learn, NumPy, SciPy          |
| API               | FastAPI, Uvicorn, Pydantic          |

## Project Structure

```
semantic-search-system/
├── api/               # FastAPI application and endpoints
├── cache/             # Query caching logic
├── clustering/        # Document clustering
├── data/              # Source dataset / documents
├── embeddings/        # Embedding generation
├── vector_db/         # FAISS vector index storage and search
├── requirements.txt   # Python dependencies
├── test_cache.py      # Tests for the cache
├── test_pipeline.py   # Tests for the full pipeline
└── README.md
```

## How It Works

1. **Load data**: documents are read from `data/`.
2. **Embed**: each document is converted into a vector using a sentence-transformers model.
3. **Cluster**: embeddings are grouped into clusters to organise the corpus.
4. **Index**: vectors are stored in a FAISS index (`vector_db/`).
5. **Query**: a search query is embedded the same way and the closest vectors are retrieved.
6. **Cache**: results for previous queries are cached so repeated searches return faster.
7. **Serve**: the whole pipeline is exposed through a FastAPI service in `api/`.

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### Installation

```bash
git clone https://github.com/Shrijeet-Ambastha/semantic-search-system.git
cd semantic-search-system

# optional but recommended
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

> The first run downloads the embedding model from Hugging Face, so an internet connection is needed once.

### Run the API

```bash
uvicorn api.main:app --reload
```

> Replace `api.main:app` with the actual module and app name in your `api/` folder if different.

Interactive API docs are then available at `http://127.0.0.1:8000/docs`.

### Run the tests

```bash
python test_cache.py
python test_pipeline.py
```

## Example Usage

```bash
curl "http://127.0.0.1:8000/search?query=your+search+text"
```

> Adjust the endpoint path and parameters to match your API.

## Configuration

Settings such as the embedding model, number of clusters and number of results to return can be changed in the corresponding modules (`embeddings/`, `clustering/`, `vector_db/`).

## Future Improvements

- Support for larger datasets with approximate indexes (IVF, HNSW)
- GPU-enabled FAISS
- Persistent cache (for example Redis)
- A simple web UI for searching

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a pull request

## Author

**Shrijeet Ambastha**: [GitHub](https://github.com/Shrijeet-Ambastha)
