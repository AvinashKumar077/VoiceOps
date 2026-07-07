import pandas as pd

from app.models.conversation import Conversation


class CsvParser:

    def parse(self, file) -> list[Conversation]:
        df = pd.read_csv(file)

        conversations = []

        for index, row in df.iterrows():
            conversation = Conversation(
                id=str(index),
                text=str(row["review"]),
                source="csv",
            )

            conversations.append(conversation)

        return conversations
