# pylint:disable = C0321
from typing import Optional
from abc import ABC, abstractmethod

class RequestLogsRepositoryInterface(ABC):
    @abstractmethod
    async def insert_request_logs(self, request_logs_infos: dict) -> None: pass

    @abstractmethod
    async def get_average_metrics_latency_request_logs(self, endpoint: str | None) -> list[dict]:
        pass

    @abstractmethod
    async def get_error_rate_service_request_logs(self, service:Optional[str] = None) -> list[dict]:
        pass

    @abstractmethod
    async def get_p95_latency_service_request_logs(self, service: str) -> list[dict]: pass

    @abstractmethod
    async def get_metrics_grouped_by_minute(self, service: str) -> list[dict]: pass
