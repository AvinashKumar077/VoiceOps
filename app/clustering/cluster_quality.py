import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class ClusterQuality:

    def score(
            self,
            embeddings: np.ndarray,
    ) -> float:

        if len(embeddings) <= 1:
            return 1.0

        centroid = np.mean(
            embeddings,
            axis=0,
            keepdims=True,
        )

        similarities = cosine_similarity(
            embeddings,
            centroid,
        )

        return float(
            similarities.mean()
        )