from app.models.repositories.request_logs_repository import RequestLogsRepository
from app.controllers.request_log_get_p95_latency_service import GetP95LatencyServiceRequestLogs
from app.views.request_log_get_p95_latency_service_view import RequestLogGetP95LatencyServiceView
from app.models.settings.database_connection_handler import DbConnectionHandler

def request_log_get_p95_latency_composer():
    db_handler = DbConnectionHandler
    model = RequestLogsRepository(db_handler)
    controller = GetP95LatencyServiceRequestLogs(model)
    view = RequestLogGetP95LatencyServiceView(controller)
    return view
