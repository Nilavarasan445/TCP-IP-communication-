from abc import ABC, abstractmethod

class Protocol(ABC):
    @abstractmethod
    def connect(self, host, port):
        pass

    @abstractmethod
    def send_data(self, data):
        pass

    @abstractmethod
    def receive_data(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass
