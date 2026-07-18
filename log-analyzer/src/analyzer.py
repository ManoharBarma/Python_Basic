from collections import Counter

class LogAnalyzer:
    def __init__(self, logs, config):
        self.logs = logs
        self.config = config

    def get_summary(self):
        total_logs = len(self.logs)
        if total_logs == 0:
            return {"error": "No logs found"}

        counts = Counter(log["level"] for log in self.logs)
        info_count = counts.get("INFO", 0)
        warning_count = counts.get("WARNING", 0)
        error_count = counts.get("ERROR", 0)

        error_logs = [log for log in self.logs if log["level"] == "ERROR"]
        error_messages = [log["message"] for log in error_logs]
        
        top_errors_limit = self.config.get("top_errors", 5)
        top_errors = Counter(error_messages).most_common(top_errors_limit)

        first_error = error_logs[0] if error_logs else None
        latest_error = error_logs[-1] if error_logs else None

        all_messages = [log["message"] for log in self.logs]
        top_10_messages = Counter(all_messages).most_common(10)

        hourly_counts = Counter(log["time"][:2] for log in self.logs)
        
        return {
            "total_logs": total_logs,
            "info_count": info_count,
            "warning_count": warning_count,
            "error_count": error_count,
            "error_percentage": round((error_count / total_logs) * 100, 2) if total_logs else 0,
            "warning_percentage": round((warning_count / total_logs) * 100, 2) if total_logs else 0,
            "top_errors": [{"message": msg, "count": count} for msg, count in top_errors],
            "first_error": first_error,
            "latest_error": latest_error,
            "top_10_messages": [{"message": msg, "count": count} for msg, count in top_10_messages],
            "hourly_counts": [{"hour": hour, "count": count} for hour, count in sorted(hourly_counts.items())]
        }

    def search(self, level=None, keyword=None, date=None):
        results = self.logs
        if level:
            results = [log for log in results if log["level"] == level.upper()]
        if keyword:
            results = [log for log in results if keyword.lower() in log["message"].lower()]
        if date:
            results = [log for log in results if log["date"] == date]
        return results
