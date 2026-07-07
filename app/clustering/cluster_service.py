from collections import defaultdict

import hdbscan
import numpy as np

from app.clustering.dimension_reducer import DimensionReducer
from app.clustering.models import ReviewCluster
from app.models.conversation import Conversation


class ClusterService:

    def __init__(self):

        self.reducer = DimensionReducer()

        self.clusterer = hdbscan.HDBSCAN(
            min_cluster_size=15,
            metric="euclidean",
        )

    def cluster(
            self,
            conversations: list[Conversation],
            embeddings: np.ndarray,
    ) -> list[ReviewCluster]:

        reduced = self.reducer.reduce(
            embeddings
        )

        labels = self.clusterer.fit_predict(
            reduced
        )

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
                    cluster_id=int(label),
                    size=len(reviews),
                    representative_reviews=reviews[:5],
                )

            )

        return sorted(
            clusters,
            key=lambda cluster: cluster.size,
            reverse=True,
        )
