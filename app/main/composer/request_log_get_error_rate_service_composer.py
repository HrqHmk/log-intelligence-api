from app.models.repositories.request_logs_repository import RequestLogsRepository
from app.controllers.request_log_get_error_rate_service import GetErrorRateServiceRequestLogs
from app.views.request_log_get_error_rate_service_view import RequestLogGetErrorRateServiceView
from app.models.settings.database_connection_handler import DbConnectionHandler

def request_log_get_error_rate_composer():
    db_handler = DbConnectionHandler
    model = RequestLogsRepository(db_handler)
    controller = GetErrorRateServiceRequestLogs(model)
    view = RequestLogGetErrorRateServiceView(controller)
    return view
