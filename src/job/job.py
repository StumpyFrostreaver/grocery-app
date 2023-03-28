class Job:
    def __init__(self, reader_type, url):
        self.__reader_type = reader_type
        self.__url = url

    @property
    def reader_type(self):
        return self.__reader_type

    @property
    def url(self):
        return self.__url

    @staticmethod
    def create_job(reader_type, url):
        job = Job(reader_type, url)
        return job
