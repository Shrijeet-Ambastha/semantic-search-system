from embeddings.embedder import generate_embeddings
from cache.semantic_cache import SemanticCache


cache = SemanticCache()


queries = [
    "space exploration missions",
    "NASA mission discussion",
    "computer graphics rendering"
]


for q in queries:

    emb = generate_embeddings([q])[0]

    hit, item, sim = cache.search(emb)

    if hit:
        print("\nCache Hit!")
        print("Matched Query:", item["query"])
        print("Similarity:", sim)

    else:
        print("\nCache Miss")

        result = "Some search result"

        cache.add(q, emb, result, cluster_id=0)


print("\nCache Stats:")
print(cache.stats())