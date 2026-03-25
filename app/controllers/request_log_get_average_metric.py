# pylint:disable = C0301
from app.models.repositories.interfaces.request_logs_repository import RequestLogsRepositoryInterface

class GetAverageMetricsLatencyRequestLogs:
    def __init__(self, request_log_repository: RequestLogsRepositoryInterface):
        self.request_log_repository = request_log_repository

    async def get_average_latency(self, endpoint: str) -> dict:
        response = await self.request_log_repository.get_average_metrics_latency_request_logs(endpoint)
        return {
            "Type": "Average Latency",
            "count": len(response),
            "attributes": response
        }
