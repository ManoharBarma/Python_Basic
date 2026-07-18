import os
import re

class LogParser:
    def __init__(self, log_file):
        self.log_file = log_file
        # Matches both simple format and detailed logger format
        self.pattern = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2}).*?(?P<level>INFO|WARNING|ERROR)\s+[-:]*\s*(?P<message>.*)$")
        self.valid_levels = {"INFO", "WARNING", "ERROR"}

    def parse(self):
        logs = []
        if not os.path.exists(self.log_file):
            return logs

        try:
            with open(self.log_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    match = self.pattern.match(line)
                    if match:
                        level = match.group("level")
                        if level in self.valid_levels:
                            logs.append({
                                "date": match.group("date"),
                                "time": match.group("time"),
                                "datetime": f"{match.group('date')} {match.group('time')}",
                                "level": level,
                                "message": match.group("message")
                            })
        except Exception:
            # Handle bad files gracefully
            pass

        return logs
