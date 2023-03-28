class Job:
    def __init__(self, reader_type, product_type, url):
        self.__reader_type = reader_type
        self.__product_type = product_type
        self.__url = url

    @property
    def reader_type(self):
        return self.__reader_type

    @property
    def product_type(self):
        return self.__product_type

    @property
    def url(self):
        return self.__url

    @property
    def name(self):
        return f"{self.reader_type} - {self.product_type}"

    @staticmethod
    def create_job(reader_type, product_type, url):
        job = Job(reader_type, product_type, url)
        return job
