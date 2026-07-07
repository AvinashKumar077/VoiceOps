from collections import defaultdict

import hdbscan
import numpy as np

from app.clustering.cluster_quality import ClusterQuality
from app.clustering.dimension_reducer import DimensionReducer
from app.clustering.models import ReviewCluster
from app.clustering.representative_selector import RepresentativeSelector
from app.models.conversation import Conversation


class ClusterService:

    def __init__(self):

        self.reducer = DimensionReducer()

        self.clusterer = hdbscan.HDBSCAN(
            min_cluster_size=15,
            metric="euclidean",
        )

        self.selector = RepresentativeSelector()
        self.quality = ClusterQuality()

    def cluster(
            self,
            conversations: list[Conversation],
            embeddings: np.ndarray,
    ) -> list[ReviewCluster]:

        # Reduce embedding dimensions before clustering
        reduced_embeddings = self.reducer.reduce(
            embeddings
        )

        # Generate cluster labels
        labels = self.clusterer.fit_predict(
            reduced_embeddings
        )

        # Group conversations and embeddings by cluster
        grouped = defaultdict(list)

        for i, (conversation, label) in enumerate(
                zip(conversations, labels)
        ):

            # Ignore noise
            if label == -1:
                continue

            grouped[label].append(
                (
                    conversation,
                    embeddings[i],
                )
            )

        clusters = []

        # Build ReviewCluster objects
        for label, items in grouped.items():

            reviews = [
                item[0].text
                for item in items
            ]

            cluster_embeddings = np.array(
                [
                    item[1]
                    for item in items
                ]
            )

            representative_reviews = self.selector.select(
                cluster_embeddings,
                reviews,
            )

            average_similarity = self.quality.score(
                cluster_embeddings
            )

            clusters.append(
                ReviewCluster(
                    cluster_id=int(label),
                    size=len(reviews),
                    representative_reviews=representative_reviews,
                    average_similarity=average_similarity,
                )
            )

        return sorted(
            clusters,
            key=lambda cluster: (
                cluster.size,
                cluster.average_similarity,
            ),
            reverse=True,
        )