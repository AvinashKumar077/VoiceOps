from app.embeddings.embedding_service import EmbeddingService
from app.clustering.cluster_service import ClusterService

texts = [
    "Payment failed",
    "Unable to pay",
    "Money deducted but recharge failed",
    "Login failed",
    "Cannot login",
    "OTP not received",
    "Weather is beautiful",
    "I love pizza",
]

embedding_service = EmbeddingService()
cluster_service = ClusterService()

embeddings = embedding_service.embed_batch(texts)

labels = cluster_service.cluster(embeddings)

for text, label in zip(texts, labels):
    print(f"[{label}] {text}")
