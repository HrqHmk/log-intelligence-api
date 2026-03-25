import pytest
from .request_log_get_average_metric import GetAverageMetricsLatencyRequestLogs

class RequestLogRepositoryMock:
    def __init__(self):
        self.endpoint = ""

    async def get_average_metrics_latency_request_logs(self, endpoint:str)-> list[dict]:
        self.endpoint = endpoint
        return [{"response_time_ms": 100}, {"response_time_ms": 200}]

@pytest.mark.asyncio
async def test_get_average_metrics_latency_request_logs():
    request_log_repository = RequestLogRepositoryMock()
    request_log_get_average = GetAverageMetricsLatencyRequestLogs(request_log_repository)

    response = await request_log_get_average.get_average_latency("/api/users")
    assert response["Type"] == "Average Latency"
    assert response["count"] == 2
    assert response["attributes"][0]["response_time_ms"] == 100
    assert response["attributes"][1]["response_time_ms"] == 200
