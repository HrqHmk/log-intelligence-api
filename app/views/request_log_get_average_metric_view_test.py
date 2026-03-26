import pytest
from .request_log_get_average_metric_view import RequestLogGetAverageMetricView
from .http_types.http_request import HttpRequest

class RequestLogControllerMock:
    def __init__(self):
        self.get_called = False
        self.endpoint = ""

    async def get_average_metrics_latency(self, endpoint: str):
        self.get_called = True
        self.endpoint = endpoint

@pytest.mark.asyncio
async def test_handle_get_average_metrics_latency():
    controller_mock = RequestLogControllerMock()
    view = RequestLogGetAverageMetricView(controller_mock)
    http_request = HttpRequest(
        path_params={"endpoint": "user-service"}
    )

    response = await view.handle_insert_request_log(http_request)

    assert controller_mock.get_called is True
    assert controller_mock.endpoint == "user-service"
    assert response.status_code == 200
