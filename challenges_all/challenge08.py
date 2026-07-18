build_log = [
    "[INFO] Cloning repository...",
    "[INFO] Installing dependencies...",
    "[WARNING] Using deprecated package.",
    "[INFO] Running unit tests...",
    "[ERROR] 3 test cases failed.",
    "[INFO] Building Docker image...",
    "[ERROR] Docker build failed.",
    "[INFO] Cleaning workspace..."
]


def analyze_build(build_log):
    info_count = 0
    warning_count = 0
    error_count = 0
    build_status = "SUCCESS"
    error_lines = []

    for log in build_log:
        log_level = log.split(maxsplit=1)[0]

        if "[info]" in log.lower():
            info_count += 1
        elif "[warning]" in log.lower():
            warning_count += 1
        elif "[error]" in log.lower():
            error_count += 1
            error_lines.append(log)
    if error_count > 0:
        build_status = "FAILED"
    summary = {
        "info": info_count,
        "warning": warning_count,
        "error": error_count,
        "status": build_status
    }
    return summary, error_lines


print(analyze_build(build_log))


#############################################################

def analyze_build(build_log: list[str]) -> tuple[dict, list[str]]:
    """
    Analyze a Jenkins build log.

    Args:
        build_log: List containing Jenkins log entries.

    Returns:
        Tuple containing:
        - Summary dictionary
        - List of error messages
    """

    # Counters for each log level
    info_count = 0
    warning_count = 0
    error_count = 0

    # Store only the actual error messages
    error_messages = []

    # Process every log line
    for log in build_log:

        # Split into:
        # [INFO] Building Docker...
        # becomes:
        # level = [INFO]
        # message = Building Docker...
        level, message = log.split(maxsplit=1)

        if level == "[INFO]":
            info_count += 1

        elif level == "[WARNING]":
            warning_count += 1

        elif level == "[ERROR]":
            error_count += 1
            error_messages.append(message)

    # Build status depends on whether any errors occurred
    build_status = "FAILED" if error_count else "SUCCESS"

    # Summary dictionary
    summary = {
        "info": info_count,
        "warning": warning_count,
        "error": error_count,
        "status": build_status,
    }

    return summary, error_messages


# ------------------------
# Example usage
# ------------------------

summary, errors = analyze_build(build_log)

print("===== Jenkins Build Summary =====")
print(f"INFO     : {summary['info']}")
print(f"WARNING  : {summary['warning']}")
print(f"ERROR    : {summary['error']}")
print(f"STATUS   : {summary['status']}")

if errors:
    print("\nFailed Steps")
    for index, error in enumerate(errors, start=1):
        print(f"{index}. {error}")
