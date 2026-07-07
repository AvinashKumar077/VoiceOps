from app.analytics.statistics_service import StatisticsService
from app.intelligence.intelligence_service import IntelligenceService
from app.parsers.csv_parser import CsvParser
from app.preprocessing.preprocessing_pipeline import PreprocessingPipeline


class UploadService:

    def __init__(self):
        self.csv_parser = CsvParser()
        self.pipeline = PreprocessingPipeline()
        self.statistics_service = StatisticsService()
        self.intelligence_service = IntelligenceService()

    def upload(self, file):

        # Parse CSV
        conversations = self.csv_parser.parse(file)

        # Clean & validate
        conversations = self.pipeline.process(conversations)

        # Generate statistics
        statistics = self.statistics_service.generate(conversations)

        # Generate intelligence
        intelligence = self.intelligence_service.analyze(conversations)

        return {
            "status": "success",
            "statistics": statistics,
            "intelligence": intelligence,
        }