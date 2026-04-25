from app.models.repositories.request_logs_repository import RequestLogsRepository
from app.controllers.request_log_get_anomaly_service import GetAnomalyServiceRequestLogs
from app.views.request_log_get_anomaly_service_view import RequestLogGetAnomalyServiceView
from app.models.settings.database_connection_handler import DbConnectionHandler

def request_log_get_anomaly_service_composer():
    db_handler = DbConnectionHandler
    model = RequestLogsRepository(db_handler)
    controller = GetAnomalyServiceRequestLogs(model)
    view = RequestLogGetAnomalyServiceView(controller)
    return view
