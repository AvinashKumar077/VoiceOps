class NGramExtractor:

    def extract(
            self,
            tokens: list[str],
            n: int = 2,
    ) -> list[str]:
        """
        Generate n-grams from a list of tokens.

        Example:
        tokens = ["payment", "failed", "today"]

        n=2 ->
        [
            "payment failed",
            "failed today"
        ]
        """

        if n <= 0:
            raise ValueError("n must be greater than 0")

        if len(tokens) < n:
            return []

        return [
            " ".join(tokens[i:i + n])
            for i in range(len(tokens) - n + 1)
        ]
