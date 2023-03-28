from src.common import reader_types

from src.reader.base_reader import BaseReader

from src.reader.no_frills_reader import NoFrillsReader
from src.reader.metro_reader import MetroReader
from src.reader.voila_reader import VoilaReader


class JobRunner:
    def __init__(self):
        self.__job = None
        self.__products = None
        pass

    def run_job(self, job):
        self.__job = job
        self.__products = None
        reader = self.__create_reader()
        self.__products = reader.parse()
        return self.__products

    def __create_reader(self) -> BaseReader:
        reader = None
        if self.__job.reader_type == reader_types.NOT_SET:
            print(f"ERROR: Job:__create_reader(): 'reader_type' not set on job: '{self.__job}'")
        elif self.__job.reader_type == reader_types.NO_FRILLS:
            reader = NoFrillsReader(self.__job)
        elif self.__job.reader_type == reader_types.METRO:
            reader = MetroReader(self.__job)
        elif self.__job.reader_type == reader_types.VOILA:
            reader = VoilaReader(self.__job)
        else:
            print(f"ERROR: Job:__create_reader(): Unknown 'reader_type' found: '{str(self.__job.reader_type)}")

        return reader

    def dump_to_csv(self, file_name):
        product_count = 0
        with open(file_name, 'w', encoding="utf-8", newline='') as file:
            for product in self.__products:
                product_count += 1
                if product_count == 1:
                    file.write(product.as_csv_header()+'\n')

                file.write(product.as_csv+'\n')
        print(f"Dumped results to csv file: '{file_name}'")
