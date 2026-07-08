from app.clustering.models import ReviewCluster


class BatchPromptBuilder:

    def build(
            self,
            clusters: list[ReviewCluster],
    ) -> str:
        clusters_text = "\n----------------\n".join(
            self._render_cluster(cluster)
            for cluster in clusters
        )

        return f"""
You are a senior product analyst.
Analyze every customer issue cluster below.

{clusters_text}

Return ONLY a valid JSON array, one object per cluster, using the exact
cluster_id given above so each insight can be matched back to its cluster:
[
{{
"cluster_id":0,
"title":"",
"summary":"",
"sentiment":"Positive|Negative|Mixed",
"severity":"Low|Medium|High|Critical",
"business_impact":"Low|Medium|High",
"engineering_effort":"Low|Medium|High",
"recommended_priority":"P0|P1|P2|P3"
}}
]
"""

    @staticmethod
    def _render_cluster(cluster: ReviewCluster) -> str:
        reviews_text = "\n".join(
            f"- {review}"
            for review in cluster.representative_reviews
        )

        return f"""Cluster ID: {cluster.cluster_id}
Size: {cluster.size}
Representative Reviews:
{reviews_text}"""
