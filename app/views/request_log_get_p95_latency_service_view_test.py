import pytest
from .request_log_get_p95_latency_service_view import RequestLogGetP95LatencyServiceView
from .http_types.http_request import HttpRequest

class RequestLogControllerMock:
    def __init__(self):
        self.get_called = False
        self.service = ""

    async def get_p95_latency_service(self, service: str):
        self.get_called = True
        self.service = service

@pytest.mark.asyncio
async def test_handle_get_p95_latency_service():
    controller_mock = RequestLogControllerMock()
    view = RequestLogGetP95LatencyServiceView(controller_mock)
    http_request = HttpRequest(
        path_params={"service": "user-service"}
    )

    response = await view.handle_insert_request_log(http_request)

    assert controller_mock.get_called is True
    assert controller_mock.service == "user-service"
    assert response.status_code == 200
