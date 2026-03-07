import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class SemanticCache:

    def __init__(self, threshold=0.85):

        self.cache = []

        self.threshold = threshold

        self.hit_count = 0
        self.miss_count = 0


    def search(self, query_embedding):

        for item in self.cache:

            similarity = cosine_similarity(
                [query_embedding],
                [item["embedding"]]
            )[0][0]

            if similarity >= self.threshold:

                self.hit_count += 1

                return True, item, similarity

        self.miss_count += 1

        return False, None, 0


    def add(self, query, embedding, result, cluster_id):

        self.cache.append({
            "query": query,
            "embedding": embedding,
            "result": result,
            "cluster": cluster_id
        })


    def stats(self):

        total = len(self.cache)

        hit_rate = 0

        if (self.hit_count + self.miss_count) > 0:
            hit_rate = self.hit_count / (self.hit_count + self.miss_count)

        return {
            "total_entries": total,
            "hit_count": self.hit_count,
            "miss_count": self.miss_count,
            "hit_rate": hit_rate
        }


    def clear(self):

        self.cache = []
        self.hit_count = 0
        self.miss_count = 0