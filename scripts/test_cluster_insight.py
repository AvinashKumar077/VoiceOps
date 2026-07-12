from app.clustering.models import ReviewCluster
from app.insights.batch_insight_service import BatchInsightService

cluster = ReviewCluster(
    cluster_id=56,
    size=277,
    average_similarity=0.91,
    representative_reviews=[
        "Unable to login",
        "OTP not received",
        "Cannot sign in",
        "Forced sign in",
        "Need to create an account to use it."
    ]
)

service = BatchInsightService()

insights = service.analyze([cluster])

for insight in insights:
    print(insight.model_dump_json(indent=2))
