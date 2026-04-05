from app.models.repositories.request_logs_repository import RequestLogsRepository
from app.controllers.request_log_insert import RequestLogInsert
from app.views.request_log_insert_view import RequestLogInsertView
from app.models.settings.database_connection_handler import DbConnectionHandler

def request_log_insert_composer():
    db_handler = DbConnectionHandler
    model = RequestLogsRepository(db_handler)
    controller = RequestLogInsert(model)
    view = RequestLogInsertView(controller)
    return view
