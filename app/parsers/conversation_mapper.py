from datetime import datetime

import pandas as pd

from app.models.conversation import Conversation
from app.parsers.header_detector import HeaderMapping


class ConversationMapper:

    def map(
            self,
            row: pd.Series,
            mapping: HeaderMapping
    ) -> Conversation:

        return Conversation(
            id=str(row[mapping.id_column]) if mapping.id_column else "",

            text=str(row[mapping.text_column]),

            source="csv",

            rating=int(row[mapping.rating_column])
            if mapping.rating_column and pd.notna(row[mapping.rating_column])
            else None,

            created_at=self.parse_date(
                row[mapping.date_column]
            ) if mapping.date_column else None,
        )

    @staticmethod
    def parse_date(value):

        if pd.isna(value):
            return None

        try:
            return pd.to_datetime(value)
        except Exception:
            return None
