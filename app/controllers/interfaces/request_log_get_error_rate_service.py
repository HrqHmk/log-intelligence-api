from abc import ABC, abstractmethod

class GetErrorRateServiceRequestLogsInterface(ABC):
    @abstractmethod
    def get_error_rate_service(self, service: str) -> dict:
        pass
