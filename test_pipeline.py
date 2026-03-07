from data.dataset_loader import load_dataset
from embeddings.embedder import generate_embeddings
from vector_db.faiss_store import VectorStore
from clustering.fuzzy_cluster import run_fuzzy_clustering


texts, labels = load_dataset()

# use smaller sample for clustering
texts = texts[:1000]

embeddings = generate_embeddings(texts)

dimension = len(embeddings[0])

vector_db = VectorStore(dimension)
vector_db.add_documents(embeddings, texts)

print("Vector database ready!")

# run clustering
centers, membership = run_fuzzy_clustering(embeddings, 10)

print("Fuzzy clustering completed!")
print("Cluster membership shape:", membership.shape)
doc_id = 5

print("\nCluster distribution for document", doc_id)

for i, prob in enumerate(membership[:, doc_id]):
    print(f"Cluster {i}: {prob:.3f}")