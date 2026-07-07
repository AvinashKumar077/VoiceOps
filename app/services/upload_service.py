from app.parsers.csv_parser import CsvParser
from app.preprocessing.preprocessing_pipeline import PreprocessingPipeline


class UploadService:

    def __init__(self):
        self.csv_parser = CsvParser()
        self.pipeline = PreprocessingPipeline()

    def upload(self, file):
        conversations = self.csv_parser.parse(file)

        return self.pipeline.process(conversations)