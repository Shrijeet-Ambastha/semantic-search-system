import numpy as np
import skfuzzy as fuzz


def run_fuzzy_clustering(embeddings, num_clusters=10):

    # transpose for fuzzy clustering
    data = np.array(embeddings).T

    cntr, u, _, _, _, _, _ = fuzz.cluster.cmeans(
        data,
        num_clusters,
        m=2,
        error=0.005,
        maxiter=1000
    )

    return cntr, u