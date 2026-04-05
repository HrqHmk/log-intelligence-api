from app.models.repositories.request_logs_repository import RequestLogsRepository
from app.controllers.request_log_get_average_metric import GetAverageMetricsLatencyRequestLogs
from app.views.request_log_get_average_metric_view import RequestLogGetAverageMetricView
from app.models.settings.database_connection_handler import DbConnectionHandler

def request_log_get_average_metric_composer():
    db_handler = DbConnectionHandler
    model = RequestLogsRepository(db_handler)
    controller = GetAverageMetricsLatencyRequestLogs(model)
    view = RequestLogGetAverageMetricView(controller)
    return view
