import pytest
from .request_log_insert import RequestLogInsert

class RequestLogRepositoryMock:
    def __init__(self):
        self.inserted_logs = {}

    async def insert_request_logs(self, request_log:dict)-> None:
        self.inserted_logs["request_log"] = request_log

@pytest.mark.asyncio
async def test_register_request_log():
    request_log_repository = RequestLogRepositoryMock()
    request_log_insert = RequestLogInsert(request_log_repository)

    request_log_data = {
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

    response = await request_log_insert.register_request_log(request_log_data)
    assert request_log_repository.inserted_logs["request_log"] == request_log_data
    assert response["Type"] == "RequestLog"
    assert response["count"] == 1
    assert response["attributes"]["method"] == "GET"
