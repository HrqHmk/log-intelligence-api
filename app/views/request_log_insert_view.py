from app.controllers.interfaces.request_log_insert import RequestLogInsertInterface
from app.errors.error_handler import error_handler
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class RequestLogInsertView:
    def __init__(self, controller: RequestLogInsertInterface):
        self.__controller = controller

    async def handle_insert_request_log(self, http_request: HttpRequest) -> HttpResponse:
        try:
            request_log_data = http_request.body
            response = await self.__controller.register_request_log(request_log_data)
            return HttpResponse(body=response, status_code=201)
        except Exception as exception:
            error_handler(exception)
