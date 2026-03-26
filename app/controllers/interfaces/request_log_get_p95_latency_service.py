from abc import ABC, abstractmethod

class GetP95LatencyServiceRequestLogsInterface(ABC):
    @abstractmethod
    def get_p95_latency_service(self, service: str) -> dict:
        pass
