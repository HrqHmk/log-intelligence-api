# pylint:disable = C0301
from app.models.repositories.interfaces.request_logs_repository import RequestLogsRepositoryInterface

class GetErrorRateServiceRequestLogs:
    def __init__(self, request_log_repository: RequestLogsRepositoryInterface):
        self.request_log_repository = request_log_repository

    async def get_error_rate_service(self, service: str) -> dict:
        response = await self.request_log_repository.get_error_rate_service_request_logs(service)
        return {
            "Type": "Error Rate Service",
            "count": len(response),
            "attributes": response
        }
