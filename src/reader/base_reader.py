from abc import abstractmethod, ABCMeta


class BaseReader:
    __metaclass__ = ABCMeta

    def __init__(self, job):
        self.__reader_type = job.reader_type
        self.__product_type = job.product_type
        self.__url = job.url

    @property
    def reader_type(self):
        return self.__reader_type

    @property
    def product_type(self):
        return self.__product_type

    @property
    def url(self):
        return self.__url

    @abstractmethod
    def parse(self):
        raise NotImplemented
