import time

from app.clustering.cluster_service import ClusterService
from app.embeddings.embedding_service import EmbeddingService
from app.insights.insight_service import InsightService
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

print("=" * 80)
print(f"Cluster: {cluster.cluster_id}")
print(f"Size: {cluster.size}")
print(f"Quality: {cluster.average_similarity:.3f}")

print("\nRepresentative Reviews:\n")

for review in cluster.representative_reviews:
    print(f"• {review}")

# Only send the largest, most impactful clusters to the LLM
top_clusters = clusters[:20]

insight_service = InsightService()

for cluster in top_clusters:
    insight = insight_service.analyze(cluster)

    print()
    print("=" * 80)
    print(f"Cluster: {cluster.cluster_id} (size={cluster.size})")
    print(f"Title: {insight.title}")
    print(f"Summary: {insight.summary}")
    print(f"Sentiment: {insight.sentiment}")
    print(f"Severity: {insight.severity}")
    print(f"Business Impact: {insight.business_impact}")
    print(f"Engineering Effort: {insight.engineering_effort}")
    print(f"Recommended Priority: {insight.recommended_priority}")
