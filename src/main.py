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
        try:
            with open (self.header_file, 'r') as head:
                  headers = [ column_label for column_label in  head.read().split('\n') if column_label != '']
                  header_row = '|'.join(headers) 
                  with open(self.out_file, 'a') as new:
                        new.write(str(header_row))
                        new.write('\n')
                        with open (self.data_file, 'r') as csv_file:
                              for line in csv_file.read():
                                new.write(line)
        except Exception as err:
                logger.error('Could not process the ouput file due to {}.\
                    Appending headers was unsuccessful'.format(err))
        else:
              self.load_file_to_database(self.out_file)

if __name__ == "__main__":
    EtlScript().run()
