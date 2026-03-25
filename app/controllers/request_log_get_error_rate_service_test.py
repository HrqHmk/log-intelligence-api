import pytest
from .request_log_get_error_rate_service import GetErrorRateServiceRequestLogs

class RequestLogRepositoryMock:
    def __init__(self):
        self.service = ""

    async def get_error_rate_service_request_logs(self, service:str)-> list[dict]:
        self.service = service
        return [
            {"service": service, "error_rate": 0.1},
            {"service": service, "error_rate": 0.2}
        ]

@pytest.mark.asyncio
async def test_get_error_rate_service_request_logs():
    request_log_repository = RequestLogRepositoryMock()
    request_log_get_error_rate = GetErrorRateServiceRequestLogs(request_log_repository)

    response = await request_log_get_error_rate.get_error_rate_service("/api/users")
    assert response["Type"] == "Error Rate Service"
    assert response["count"] == 2
    assert response["attributes"][0]["error_rate"] == 0.1
    assert response["attributes"][1]["error_rate"] == 0.2
