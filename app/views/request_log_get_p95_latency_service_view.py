from app.controllers.interfaces.request_log_get_p95_latency_service import GetP95LatencyServiceRequestLogsInterface
from app.errors.error_handler import error_handler
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class RequestLogGetP95LatencyServiceView:
    def __init__(self, controller: GetP95LatencyServiceRequestLogsInterface):
        self.__controller = controller

    async def handle_insert_request_log(self, http_request: HttpRequest) -> HttpResponse:
        try:
            service = http_request.path_params["service"]
            response = await self.__controller.get_p95_latency_service(service)
            return HttpResponse(body=response, status_code=200)
        except Exception as exception:
            error_handler(exception)
