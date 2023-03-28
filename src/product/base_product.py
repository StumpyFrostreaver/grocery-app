from abc import abstractmethod, ABCMeta


class BaseProduct:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def as_csv_header():
        return NotImplemented

    @property
    @abstractmethod
    def as_csv(self):
        return NotImplemented
