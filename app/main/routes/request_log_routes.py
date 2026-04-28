from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.views.http_types.http_request import HttpRequest
from app.validators.request_log_validator import RequestLogInput

from app.main.composer.request_log_get_error_rate_service_composer import request_log_get_error_rate_composer
from app.main.composer.request_log_get_average_metric_composer import request_log_get_average_metric_composer
from app.main.composer.request_log_get_p95_latency_service_composer import request_log_get_p95_latency_composer
from app.main.composer.request_log_insert_composer import request_log_insert_composer
from app.main.composer.request_log_get_anomaly_service_composer import request_log_get_anomaly_service_composer

request_log_routes = APIRouter(tags=["Request Logs"])

@request_log_routes.post("/request-logs")
async def insert_request_log(body: RequestLogInput):
    http_request = HttpRequest(body=body.model_dump())
    request_log_insert = request_log_insert_composer()

    http_response = await request_log_insert.handle_insert_request_log(http_request)
    return JSONResponse (
        content=jsonable_encoder(http_response.body),
        status_code=http_response.status_code
    )

@request_log_routes.get("/request-logs/error-rate/{service}")
async def get_error_rate(service: str):
    http_request = HttpRequest(path_params={"service": service})
    request_log_error_rate = request_log_get_error_rate_composer()
    http_response = await request_log_error_rate.handle_get_request_log_error_rate(http_request)
    return JSONResponse (
        content=http_response.body,
        status_code=http_response.status_code
    )

@request_log_routes.get("/request-logs/metrics/average-latency/{endpoint}")
async def get_average_metric(endpoint: str):
    http_request = HttpRequest(path_params={"endpoint": endpoint})
    request_log_average_metric = request_log_get_average_metric_composer()
    http_response = await request_log_average_metric.handle_get_request_log_average_metric(http_request)
    return JSONResponse (
        content=http_response.body,
        status_code=http_response.status_code
    )

@request_log_routes.get("/request-logs/p95-latency/{service}")
async def get_p95_latency(service: str):
    http_request = HttpRequest(path_params={"service": service})
    request_log_p95_latency = request_log_get_p95_latency_composer()
    http_response = await request_log_p95_latency.handle_get_request_log_p95_latency(http_request)
    return JSONResponse (
        content=http_response.body,
        status_code=http_response.status_code
    )

@request_log_routes.get("/request-logs/anomalies/{service}")
async def get_anomaly_service(service: str):
    http_request = HttpRequest(path_params={"service": service})
    request_log_anomaly_service = request_log_get_anomaly_service_composer()
    http_response = await request_log_anomaly_service.handle_get_request_log_anomaly_service(http_request)
    return JSONResponse (
        content=http_response.body,
        status_code=http_response.status_code
    )
