from abc import abstractmethod, ABCMeta


class BaseReader:
    __metaclass__ = ABCMeta

    def __init__(self, job):
        self.__url = job.url
        self.__reader_type = job.reader_type

    @property
    def url(self):
        return self.__url

    @property
    def reader_type(self):
        return self.__reader_type

    @abstractmethod
    def parse(self):
        raise NotImplemented
