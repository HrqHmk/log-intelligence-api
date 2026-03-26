from abc import ABC, abstractmethod

class GetAverageMetricsLatencyRequestLogsInterface(ABC):
    @abstractmethod
    def get_average_latency(self, endpoint: str) -> dict:
        pass
