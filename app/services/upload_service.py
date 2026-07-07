from app.parsers.csv_parser import CsvParser


class UploadService:

    def __init__(self):
        self.csv_parser = CsvParser()

    def upload(self, file):
        return self.csv_parser.parse(file)
