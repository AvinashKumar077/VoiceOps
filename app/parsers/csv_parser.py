import pandas as pd

from app.models.conversation import Conversation
from app.parsers.conversation_mapper import ConversationMapper
from app.parsers.header_detector import HeaderDetector
import time

class CsvParser:

    def __init__(self):
        self.header_detector = HeaderDetector()
        self.mapper = ConversationMapper()

    def parse(self, file) -> list[Conversation]:
        start = time.perf_counter()
        df = pd.read_csv(file)
        print(f"Read CSV: {time.perf_counter() - start:.3f}s")
        start = time.perf_counter()
        mapping = self.header_detector.detect(df.columns.tolist())
        print(f"Mapping: {time.perf_counter() - start:.3f}s")

        conversations = []

        for _, row in df.iterrows():
            conversation = self.mapper.map(row, mapping)
            conversations.append(conversation)

        return conversations