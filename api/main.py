from fastapi import FastAPI
from pydantic import BaseModel

from embeddings.embedder import generate_embeddings
from cache.semantic_cache import SemanticCache

app = FastAPI()

cache = SemanticCache()


class QueryRequest(BaseModel):
    query: str


@app.post("/query")
def query_api(request: QueryRequest):

    query = request.query

    embedding = generate_embeddings([query])[0]

    hit, item, sim = cache.search(embedding)

    if hit:

        return {
            "query": query,
            "cache_hit": True,
            "matched_query": item["query"],
            "similarity_score": float(sim),
            "result": item["result"],
            "dominant_cluster": item["cluster"]
        }

    # simulate search result
    result = "Top documents related to query"

    cache.add(query, embedding, result, cluster_id=0)

    return {
        "query": query,
        "cache_hit": False,
        "matched_query": None,
        "similarity_score": 0,
        "result": result,
        "dominant_cluster": 0
    }


@app.get("/cache/stats")
def cache_stats():

    return cache.stats()


@app.delete("/cache")
def clear_cache():

    cache.clear()

    return {"message": "Cache cleared"}