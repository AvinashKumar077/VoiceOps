import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class RepresentativeSelector:

    def select(
            self,
            embeddings: np.ndarray,
            reviews: list[str],
            top_k: int = 5,
    ) -> list[str | list[str]] | list[str]:
        if len(reviews) <= top_k:
            return reviews

        centroid = np.mean(
            embeddings,
            axis=0,
            keepdims=True,
        )

        similarities = cosine_similarity(
            embeddings,
            centroid,
        ).flatten()

        indices = np.argsort(
            similarities
        )[::-1][:top_k]

        return [
            reviews[i]
            for i in indices
        ]
