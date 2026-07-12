from app.embeddings.embedding_service import EmbeddingService


def test_embedding():

    service = EmbeddingService()

    embedding = service.embed(
        "Payment failed"
    )

    assert len(embedding) == 384