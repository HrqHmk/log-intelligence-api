from abc import ABC, abstractmethod

class GetAnomalyServiceRequestLogsInterface(ABC):
    @abstractmethod
    def get_anomaly_service_request_logs(self, endpoint: str) -> dict:
        pass
