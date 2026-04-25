from sklearn.ensemble import IsolationForest

class AnomalyDetectionService:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def detect_anomalies(self, data: list[dict]) -> list[dict]:
        if len(data) < 5:
            return []

        x = [
            [row["average_latency_ms"], row["error_rate"]]
            for row in data
        ]

        self.model.fit(x)
        predictions = self.model.predict(x)
        scores = self.model.decision_function(x)

        result = []
        for row, pred, score in zip(data, predictions, scores):
            if pred == -1:
                result.append({
                    **row,
                    "anomaly": True,
                    "anomaly_score": round(float(score), 2)
                })

        return result
