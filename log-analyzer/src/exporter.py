import json
import csv
import os
from datetime import datetime

class Exporter:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def export_json(self, summary_data):
        file_path = os.path.join(self.output_dir, "summary.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(summary_data, f, indent=4)
        return file_path

    def export_csv(self, summary_data):
        file_path = os.path.join(self.output_dir, "summary.csv")
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Value"])
            if "error" in summary_data:
                writer.writerow(["Error", summary_data["error"]])
                return file_path

            writer.writerow(["Total Logs", summary_data["total_logs"]])
            writer.writerow(["INFO Count", summary_data["info_count"]])
            writer.writerow(["WARNING Count", summary_data["warning_count"]])
            writer.writerow(["ERROR Count", summary_data["error_count"]])
            writer.writerow(["ERROR %", summary_data["error_percentage"]])
            writer.writerow(["WARNING %", summary_data["warning_percentage"]])
            
            writer.writerow([])
            writer.writerow(["Top Errors", "Count"])
            for err in summary_data["top_errors"]:
                writer.writerow([err["message"], err["count"]])

            writer.writerow([])
            writer.writerow(["Hourly Counts (Hour)", "Count"])
            for h in summary_data["hourly_counts"]:
                writer.writerow([h["hour"], h["count"]])
                
        return file_path

    def export_html(self, summary_data):
        file_path = os.path.join(self.output_dir, "report.html")
        
        if "error" in summary_data:
            html = f"<html><body><h1>Error</h1><p>{summary_data['error']}</p></body></html>"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)
            return file_path

        total = summary_data["total_logs"]
        
        def make_bar(count, total, color):
            if total == 0: return ""
            width = max(1, int((count / total) * 100))
            blocks = "█" * int(width / 5)
            if not blocks and count > 0:
                blocks = "█"
            return f'<span style="color: {color}; font-family: monospace;">{blocks}</span>'

        info_bar = make_bar(summary_data["info_count"], total, "green")
        warn_bar = make_bar(summary_data["warning_count"], total, "orange")
        err_bar = make_bar(summary_data["error_count"], total, "red")

        top_errors_html = "".join([f"<li>{e['message']} ({e['count']})</li>" for e in summary_data["top_errors"]])

        generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Enterprise Log Report</title>
<style>
    body {{ font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; padding: 20px; }}
    .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
    h1, h2 {{ color: #2c3e50; }}
    .bar-row {{ display: flex; margin-bottom: 10px; align-items: center; }}
    .bar-label {{ width: 100px; font-weight: bold; }}
    .bar-value {{ flex-grow: 1; }}
    ul {{ list-style-type: none; padding: 0; }}
    li {{ padding: 5px 0; border-bottom: 1px solid #eee; }}
    .footer {{ margin-top: 30px; font-size: 0.9em; color: #777; }}
</style>
</head>
<body>
<div class="container">
    <h1>Enterprise Log Report</h1>
    
    <div class="bar-row">
        <div class="bar-label">INFO</div>
        <div class="bar-value">{info_bar}</div>
    </div>
    <div class="bar-row">
        <div class="bar-label">WARNING</div>
        <div class="bar-value">{warn_bar}</div>
    </div>
    <div class="bar-row">
        <div class="bar-label">ERROR</div>
        <div class="bar-value">{err_bar}</div>
    </div>

    <h2>Top Errors</h2>
    <ul>
        {top_errors_html}
    </ul>

    <div class="footer">
        Generated At<br>
        {generated_at}
    </div>
</div>
</body>
</html>"""

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        return file_path
