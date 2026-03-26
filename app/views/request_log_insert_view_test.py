import pytest
from .request_log_insert_view import RequestLogInsertView
from .http_types.http_request import HttpRequest

class RequestLogControllerMock:
    def __init__(self):
        self.insert_called = False
        self.insert_args: dict = {}

    async def register_request_log(self, request_log: dict):
        self.insert_called = True
        self.insert_args = request_log

@pytest.mark.asyncio
async def test_handle_insert_request_log():
    controller_mock = RequestLogControllerMock()
    view = RequestLogInsertView(controller_mock)
    http_request = HttpRequest(
        body={
            "method": "GET",
            "service": "user-service",
            "endpoint": "/api/users",
            "headers": {
                "Authorization": "Bearer token"
            },
            "status_code": 200,
            "response_time_ms": 100,
            "timestamp": "2023-01-01T00:00:00Z",
            "request_body": {"id": 1},
            "response_body": {"name": "John Doe"},
            "request_id": "req-123",
            "user_id": "user-123",
            "client_ip": "192.168.0.1",
            "error_message": None
        }
    )

    response = await view.handle_insert_request_log(http_request)

    assert controller_mock.insert_called is True
    assert controller_mock.insert_args == http_request.body
    assert response.status_code == 201
