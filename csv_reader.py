import csv
import os


class Read:
    """Class for reading csv files"""

    def __init__(self, filename):
        self.info = []
        self.name = filename
        self.__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def insert(self):
        """Insert info into table"""
        encodings = ['utf-8-sig', 'latin-1']
        for encoding in encodings:
            try:
                with open(os.path.join(self.__location__, self.name), encoding=encoding) as file:
                    rows = csv.DictReader(file)
                    for row in rows:
                        self.info.append(dict(row))
                break
            except UnicodeDecodeError:
                continue
