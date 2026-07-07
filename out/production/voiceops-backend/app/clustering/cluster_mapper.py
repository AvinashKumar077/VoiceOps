from collections import defaultdict

from app.clustering.models import ReviewCluster
from app.models.conversation import Conversation


class ClusterMapper:

    def map(
            self,
            conversations: list[Conversation],
            labels,
    ) -> list[ReviewCluster]:

        grouped = defaultdict(list)

        for conversation, label in zip(
                conversations,
                labels,
        ):

            if label == -1:
                continue

            grouped[label].append(
                conversation.text
            )

        clusters = []

        for label, reviews in grouped.items():

            clusters.append(
                ReviewCluster(
                    cluster_id=label,
                    size=len(reviews),
                    representative_reviews=reviews[:5],
                )
            )

        return clusters