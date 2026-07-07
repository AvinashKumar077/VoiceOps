import time

from app.clustering.cluster_service import ClusterService
from app.embeddings.embedding_service import EmbeddingService
from app.parsers.csv_parser import CsvParser
from app.preprocessing.preprocessing_pipeline import PreprocessingPipeline

csv = CsvParser()
pipeline = PreprocessingPipeline()

embedding_service = EmbeddingService()
cluster_service = ClusterService()

start = time.perf_counter()

with open("sample-data/reviews.csv", "rb") as file:
    conversations = csv.parse(file)

conversations = pipeline.process(conversations)

texts = [
    c.text
    for c in conversations
]

embeddings = embedding_service.embed_batch(texts)

clusters = cluster_service.cluster(
    conversations,
    embeddings,
)

print(f"Clusters: {len(clusters)}")

for cluster in clusters[:10]:

    print()

    print("=" * 60)
    print(cluster.cluster_id)
    print(cluster.size)

    for review in cluster.representative_reviews:
        print(review[:120])