class PromptBuilder:

    def build(
            self,
            cluster_size: int,
            reviews: list[str],
    ) -> str:
        reviews_text = "\n".join(
            f"- {review}"
            for review in reviews
        )

        return f"""
You are a senior product analyst.
Analyze this customer issue cluster.

Cluster Size:
{cluster_size}

Representative Reviews:
{reviews_text}

Return ONLY valid JSON:
{{
"title":"",
"summary":"",
"sentiment":"Positive|Negative|Mixed",
"severity":"Low|Medium|High|Critical",
"business_impact":"Low|Medium|High",
"engineering_effort":"Low|Medium|High",
"recommended_priority":"P0|P1|P2|P3"
}}
"""