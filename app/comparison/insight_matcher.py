import numpy as np
from pydantic import BaseModel

from app.comparison.models import IssueFingerprint

SIMILARITY_THRESHOLD = 0.6


class MatchedPair(BaseModel):
    previous: IssueFingerprint
    current: IssueFingerprint


class MatchResult(BaseModel):
    model_config = {"arbitrary_types_allowed": True}

    matched: list[MatchedPair]
    new_fingerprints: list[IssueFingerprint]
    resolved_fingerprints: list[IssueFingerprint]


class InsightMatcher:
    """Matches insights across two reports by embedding similarity.

    Titles alone drift between runs ("Reminder Notifications Broken" vs
    "Reminder Failure"), so exact/string matching would miss real matches.
    Embeddings let semantically equivalent issues match regardless of
    exact wording.
    """

    def match(
            self,
            previous: list[IssueFingerprint],
            current: list[IssueFingerprint],
    ) -> MatchResult:

        remaining_current = list(current)
        matched = []

        for previous_fp in previous:
            best_match, best_score = self._best_match(
                previous_fp,
                remaining_current,
            )

            if best_match is not None:
                matched.append(
                    MatchedPair(
                        previous=previous_fp,
                        current=best_match,
                    )
                )
                remaining_current.remove(best_match)

        matched_previous_ids = {
            id(pair.previous)
            for pair in matched
        }

        resolved_fingerprints = [
            fp
            for fp in previous
            if id(fp) not in matched_previous_ids
        ]

        return MatchResult(
            matched=matched,
            new_fingerprints=remaining_current,
            resolved_fingerprints=resolved_fingerprints,
        )

    @staticmethod
    def _best_match(
            target: IssueFingerprint,
            candidates: list[IssueFingerprint],
    ) -> tuple[IssueFingerprint | None, float]:

        best_match = None
        best_score = SIMILARITY_THRESHOLD

        target_embedding = np.array(target.embedding)

        for candidate in candidates:
            score = float(
                np.dot(target_embedding, np.array(candidate.embedding))
            )

            if score > best_score:
                best_score = score
                best_match = candidate

        return best_match, best_score
