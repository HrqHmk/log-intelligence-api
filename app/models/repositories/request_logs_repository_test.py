from datetime import datetime, UTC
import pytest
from app.models.settings.database_connection_handler import DbConnectionHandler
from .request_logs_repository import RequestLogsRepository

@pytest.mark.asyncio
async def test_insert_request_logs(session_factory):
    repository = RequestLogsRepository(
        lambda: DbConnectionHandler(session_factory)
    )

    request_logs_infos = {
        "timestamp": datetime.now(UTC),
        "http_method": "GET",
        "headers": {"Content-Type": "application/json"},
        "service": "test_service",
        "endpoint": "/test-endpoint",
        "request_body": {"key": "value"},
        "response_body": {"result": "success"},
        "response_time_ms": 100,
        "status_code": 200,
        "user_id": None,
        "request_id": "123e4567-e89b-12d3-a456-426614174000",
        "client_ip": "192.168.1.1"
    }

    await repository.insert_request_logs(request_logs_infos)

@pytest.mark.asyncio
async def test_get_average_metrics_latency_request_logs_with_endpoint(session_factory):
    repository = RequestLogsRepository(
        lambda: DbConnectionHandler(session_factory)
    )

    endpoint = "/checkout"
    response = await repository.get_average_metrics_latency_request_logs(endpoint)
    assert "average_latency_ms" in response[0]
    assert isinstance(response[0]["average_latency_ms"], (float, type(None)))

@pytest.mark.asyncio
async def test_get_average_metrics_latency_request_logs_without_endpoint(session_factory):
    repository = RequestLogsRepository(
        lambda: DbConnectionHandler(session_factory)
    )

    response = await repository.get_average_metrics_latency_request_logs(None)
    assert isinstance(response, list)
    for item in response:
        assert "endpoint" in item
        assert "average_latency_ms" in item
        assert isinstance(item["endpoint"], str)
        assert isinstance(item["average_latency_ms"], (float, type(None)))

@pytest.mark.asyncio
async def test_get_error_rate_request_logs(session_factory):
    repository = RequestLogsRepository(
        lambda: DbConnectionHandler(session_factory)
    )

    service = "checkout-service"
    response = await repository.get_error_rate_service_request_logs(service)
    for item in response:
        assert "service" in item
        assert "error_rate" in item
        assert isinstance(item["service"], str)
        assert isinstance(item["error_rate"], (float, type(None)))
        assert 0.0 <= item["error_rate"] <= 1.0
        assert item["service"] == service

@pytest.mark.asyncio
async def test_get_p95_latency_service_request_logs(session_factory):
    repository = RequestLogsRepository(
        lambda: DbConnectionHandler(session_factory)
    )

    service = "checkout-service"
    response = await repository.get_p95_latency_service_request_logs(service)
    for item in response:
        assert "service" in item
        assert "p95_latency_ms" in item
        assert isinstance(item["service"], str)
        assert isinstance(item["p95_latency_ms"], (float, type(None)))
        assert item["service"] == service
