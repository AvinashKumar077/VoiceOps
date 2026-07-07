from app.analytics.statistics_service import StatisticsService
from app.parsers.csv_parser import CsvParser
from app.preprocessing.preprocessing_pipeline import PreprocessingPipeline


class UploadService:

    def __init__(self):
        self.csv_parser = CsvParser()
        self.pipeline = PreprocessingPipeline()
        self.statistics_service = StatisticsService()

    def upload(self, file):

        conversations = self.csv_parser.parse(file)

        conversations = self.pipeline.process(conversations)

        statistics = self.statistics_service.generate(conversations)

        return {
            "status": "success",
            "statistics": statistics,
        }