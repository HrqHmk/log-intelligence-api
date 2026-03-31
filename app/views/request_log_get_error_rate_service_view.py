from app.controllers.interfaces.request_log_get_error_rate_service import GetErrorRateServiceRequestLogsInterface
from app.errors.error_handler import error_handler
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class RequestLogGetErrorRateServiceView:
    def __init__(self, controller: GetErrorRateServiceRequestLogsInterface):
        self.__controller = controller

    async def handle_get_request_log_error_rate(self, http_request: HttpRequest) -> HttpResponse:
        try:
            service = http_request.path_params["service"]
            response = await self.__controller.get_error_rate_service(service)
            return HttpResponse(body=response, status_code=200)
        except Exception as exception:
            error_handler(exception)
