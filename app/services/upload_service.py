from app.analysis.analysis_pipeline import AnalysisPipeline
from app.parsers.csv_parser import CsvParser
from app.preprocessing.preprocessing_pipeline import PreprocessingPipeline
from app.report.models import ProductAnalysisReport


class UploadService:

    def __init__(self):
        self.csv_parser = CsvParser()
        self.preprocessing_pipeline = PreprocessingPipeline()
        self.analysis_pipeline = AnalysisPipeline()

    def upload(self, file) -> ProductAnalysisReport:

        conversations = self.csv_parser.parse(file)

        conversations = self.preprocessing_pipeline.process(
            conversations
        )

        return self.analysis_pipeline.analyze(conversations)
