logs = [
    "INFO Application Started",
    "INFO Loading Config",
    "WARNING High Memory Usage",
    "ERROR Database Connection Failed",
    "INFO Retrying...",
    "ERROR Authentication Failed",
    "INFO Shutdown Complete"
]


def log_analysis(logs: dict):
    info_count = 0
    warning_count = 0
    error_count = 0

    for line in logs:
        if "error" in line.lower():
            error_count += 1
        elif "warning" in line.lower():
            warning_count += 1
        elif "info" in line.lower():
            info_count += 1
    return error_count, warning_count, info_count


log_analysis(logs)


###########################################################

def analyze_logs(logs: list[str]) -> tuple[int, int, int]:
    """
    Analyze application logs and count INFO, WARNING, and ERROR entries.

    Args:
        logs: List of log messages.

    Returns:
        Tuple containing:
            (info_count, warning_count, error_count)
    """

    info_count = 0
    warning_count = 0
    error_count = 0

    for log in logs:
        # Log level is always the first word
        log_level = log.split(maxsplit=1)[0]

        if log_level == "INFO":
            info_count += 1
        elif log_level == "WARNING":
            warning_count += 1
        elif log_level == "ERROR":
            error_count += 1

    return info_count, warning_count, error_count
