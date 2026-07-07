import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    _model = None

    def __init__(self):
        if EmbeddingService._model is None:
            EmbeddingService._model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2"
            )

    def embed(self, text: str) -> list[float]:
        return EmbeddingService._model.encode(
            text,
            normalize_embeddings=True,
        ).tolist()

    def embed_batch(
            self,
            texts: list[str],
    ) -> np.ndarray:
        return EmbeddingService._model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
