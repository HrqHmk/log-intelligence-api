import pytest
from .request_log_get_anomaly_service import GetAnomalyServiceRequestLogs

class RequestLogRepositoryMock:
    def __init__(self):
        self.service = ""

    async def get_metrics_grouped_by_minute(self, service: str) -> list[dict]:
        self.service = service
        return[
            {
                "service": "user-service",
                "minute": "2024-06-01T12:00:00",
                "average_latency_ms": 150,
                "error_rate": 0.0
            }
        ]

@pytest.mark.asyncio
async def test_get_anomaly_service_request_logs():
    request_log_repository = RequestLogRepositoryMock()
    request_log_get_anomaly = GetAnomalyServiceRequestLogs(request_log_repository)

    response = await request_log_get_anomaly.get_anomaly_service_request_logs("user-service")
    assert response["type"] == "anomaly_detection"
    assert response["count"] >= 0
    assert isinstance(response["attributes"], list)
