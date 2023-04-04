from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def build(self, data):
        pass

