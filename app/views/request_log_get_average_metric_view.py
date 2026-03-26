from app.controllers.interfaces.request_log_get_average_metric import GetAverageMetricsLatencyRequestLogsInterface
from app.errors.error_handler import error_handler
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class RequestLogGetAverageMetricView:
    def __init__(self, controller: GetAverageMetricsLatencyRequestLogsInterface):
        self.__controller = controller

    async def handle_insert_request_log(self, http_request: HttpRequest) -> HttpResponse:
        try:
            endpoint = http_request.path_params["endpoint"]
            response = await self.__controller.get_average_metrics_latency(endpoint)
            return HttpResponse(body=response, status_code=200)
        except Exception as exception:
            error_handler(exception)
