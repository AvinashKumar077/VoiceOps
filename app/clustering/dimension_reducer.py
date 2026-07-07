import numpy as np
import umap


class DimensionReducer:

    def __init__(self):
        self.reducer = umap.UMAP(
            n_neighbors=15,
            n_components=10,
            metric="cosine",
            random_state=42,
        )

    def reduce(
            self,
            embeddings: np.ndarray,
    ) -> np.ndarray:
        return self.reducer.fit_transform(
            embeddings
        )
