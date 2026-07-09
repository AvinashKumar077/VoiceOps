from app.comparison.models import TrendReport
from app.comparison.report_comparator import ReportComparator
from app.services.upload_service import UploadService


class CompareService:

    def __init__(self):
        self.upload_service = UploadService()
        self.report_comparator = ReportComparator()

    def compare(self, previous_file, current_file) -> TrendReport:

        previous_report = self.upload_service.upload(previous_file)
        current_report = self.upload_service.upload(current_file)

        return self.report_comparator.compare(
            previous_report,
            current_report,
        )
