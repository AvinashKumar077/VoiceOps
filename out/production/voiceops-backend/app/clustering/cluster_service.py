import hdbscan


class ClusterService:

    def __init__(self):

        self.clusterer = hdbscan.HDBSCAN(
            min_cluster_size=10,
            metric="euclidean",
        )

    def cluster(
            self,
            embeddings,
    ):
        """
        Returns cluster labels.

        Example:
        [0,0,1,1,-1,2]
        """

        return self.clusterer.fit_predict(
            embeddings
        )