from collections import Counter


class FrequencyAnalyzer:

    def analyze(
            self,
            tokens: list[str],
            top_n: int = 20,
    ) -> list[tuple[str, int]]:
        counter = Counter(tokens)

        return counter.most_common(top_n)
