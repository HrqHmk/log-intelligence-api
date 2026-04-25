from app.controllers.interfaces.request_log_get_anomaly_service import GetAnomalyServiceRequestLogsInterface
from app.errors.error_handler import error_handler
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class RequestLogGetAnomalyServiceView:
    def __init__(self, controller: GetAnomalyServiceRequestLogsInterface):
        self.__controller = controller

    async def handle_get_request_log_anomaly_service(self, http_request: HttpRequest) -> HttpResponse:
        try:
            service = http_request.path_params["service"]
            response = await self.__controller.get_anomaly_service_request_logs(service)
            return HttpResponse(body=response, status_code=200)
        except Exception as exception:
            error_handler(exception)
