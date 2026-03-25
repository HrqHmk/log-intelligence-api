# pylint:disable = C0301
from app.models.repositories.interfaces.request_logs_repository import RequestLogsRepositoryInterface

class GetP95LatencyServiceRequestLogs:
    def __init__(self, request_log_repository: RequestLogsRepositoryInterface):
        self.request_log_repository = request_log_repository

    async def get_p95_latency_service(self, service: str) -> dict:
        response = await self.request_log_repository.get_p95_latency_service_request_logs(service)
        return {
            "Type": "P95 Latency Service",
            "count": len(response),
            "attributes": response
        }
