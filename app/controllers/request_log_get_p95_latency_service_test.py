import pytest
from .request_log_get_p95_latency_service import GetP95LatencyServiceRequestLogs

class RequestLogRepositoryMock:
    def __init__(self):
        self.service = ""

    async def get_p95_latency_service_request_logs(self, service:str)-> list[dict]:
        self.service = service
        return [
            {"service": service, "p95_latency": 100},
            {"service": service, "p95_latency": 200}
        ]

@pytest.mark.asyncio
async def test_get_p95_latency_service_request_logs():
    request_log_repository = RequestLogRepositoryMock()
    request_log_get_p95_latency = GetP95LatencyServiceRequestLogs(request_log_repository)

    response = await request_log_get_p95_latency.get_p95_latency_service("/api/users")
    assert response["Type"] == "P95 Latency Service"
    assert response["count"] == 2
    assert response["attributes"][0]["p95_latency"] == 100
    assert response["attributes"][1]["p95_latency"] == 200
