from abc import ABC, abstractmethod

class RequestLogInsertInterface(ABC):
    @abstractmethod
    def register_request_log(self, request_log: dict) -> dict:
        pass
