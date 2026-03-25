# pylint:disable = C0301
from app.models.repositories.interfaces.request_logs_repository import RequestLogsRepositoryInterface

class RequestLogInsert:
    def __init__(self, request_log_repository: RequestLogsRepositoryInterface):
        self.request_log_repository = request_log_repository

    async def register_request_log(self, request_log:dict)-> dict:
        await self.__register_request_log(request_log)
        return self.__format_response(request_log)

    async def __register_request_log(self, request_log:dict)-> None:
        return await self.request_log_repository.insert_request_logs(request_log)

    def __format_response(self, request_log:dict)-> dict:
        return {
            "Type": "RequestLog",
            "count": 1,
            "attributes": {
                "method": request_log.get("method"),
                "service": request_log.get("service"),
                "endpoint": request_log.get("endpoint"),
                "http_method": request_log.get("http_method"),
                "headers": request_log.get("headers"),
                "status_code": request_log.get("status_code"),
                "response_time_ms": request_log.get("response_time_ms"),
                "timestamp": request_log.get("timestamp"),
                "request_body": request_log.get("request_body"),
                "response_body": request_log.get("response_body"),
                "request_id": request_log.get("request_id"),
                "user_id": request_log.get("user_id"),
                "client_ip": request_log.get("client_ip"),
                "error_message": request_log.get("error_message")
            }
        }
