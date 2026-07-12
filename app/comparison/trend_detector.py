from app.comparison.insight_matcher import MatchedPair
from app.comparison.models import Trend


class TrendDetector:

    def detect(
            self,
            matched: list[MatchedPair],
    ) -> tuple[list[Trend], list[Trend]]:

        growing = []
        shrinking = []

        for pair in matched:
            trend = self._to_trend(pair)

            if trend.change_percent > 0:
                growing.append(trend)
            elif trend.change_percent < 0:
                shrinking.append(trend)

        growing.sort(key=lambda t: t.change_percent, reverse=True)
        shrinking.sort(key=lambda t: t.change_percent)

        return growing, shrinking

    @staticmethod
    def _to_trend(pair: MatchedPair) -> Trend:
        previous_reviews = pair.previous.affected_reviews
        current_reviews = pair.current.affected_reviews

        change_percent = (
            (current_reviews - previous_reviews) / previous_reviews * 100
            if previous_reviews
            else 0.0
        )

        return Trend(
            title=pair.current.title,
            previous_reviews=previous_reviews,
            current_reviews=current_reviews,
            change_percent=round(change_percent, 1),
            direction="up" if change_percent > 0 else "down",
        )
