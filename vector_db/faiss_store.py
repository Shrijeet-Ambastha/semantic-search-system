import faiss
import numpy as np

class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add_documents(self, embeddings, texts):

        self.index.add(np.array(embeddings))
        self.documents.extend(texts)

    def search(self, query_embedding, k=5):

        D, I = self.index.search(
            np.array([query_embedding]), k
        )

        results = [self.documents[i] for i in I[0]]

        return results