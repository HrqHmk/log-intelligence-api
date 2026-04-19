class ErrorClassifierService:
    @staticmethod
    def classify_error(error_message: str) ->dict:
        message_lower = error_message.lower()

        if "timeout" in message_lower:
            return {
                "category": "Timeout Error",
                "severity": "High",
                "suggestion": "Check service latency or external dependencies."
            }

        if "connection" in message_lower:
            return {
                "category": "Connection Error",
                "severity": "Medium",
                "suggestion": "Verify network connectivity and service endpoints."
            }

        return {
            "category": "Unknown Error",
            "severity": "Low",
            "suggestion": "Review error details for further analysis."
        }
