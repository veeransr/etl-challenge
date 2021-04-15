import logging

from database import Database

logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


class EtlScript:
    def __init__(self):
        self.database_conn = Database("acme")
        self.header_file = "./headers.txt"
        self.data_file = "./data.csv"
        self.out_file = "./output.csv"

    def load_file_to_database(self, file_path: str):
        self.database_conn.load_file(file_path)

    def run(self):
        # Your code starts here.
        pass

if __name__ == "__main__":
    EtlScript().run()
