# pylint:disable = C0301
from app.models.repositories.interfaces.request_logs_repository import RequestLogsRepositoryInterface
from app.services.anomaly_detection_service import AnomalyDetectionService

class GetAnomalyServiceRequestLogs:
    def __init__(self, request_log_repository: RequestLogsRepositoryInterface):
        self.request_log_repository = request_log_repository

    async def get_anomaly_service_request_logs(self, service: str) -> dict:
        data = await self.request_log_repository.get_metrics_grouped_by_minute(service)
        anomaly_detection = AnomalyDetectionService()
        result = anomaly_detection.detect_anomalies(data)
        return {
            "type": "anomaly_detection",
            "count": len(result),
            "attributes": result
        }
