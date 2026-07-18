import argparse
import sys
import json
import os

from utils import load_config, setup_app_logging
from parser import LogParser
from analyzer import LogAnalyzer
from exporter import Exporter

def main():
    parser = argparse.ArgumentParser(description="Enterprise Log Analyzer")
    parser.add_argument("--level", help="Filter logs by level (e.g. ERROR)")
    parser.add_argument("--contains", help="Filter logs containing keyword")
    parser.add_argument("--date", help="Filter logs by date (YYYY-MM-DD)")
    parser.add_argument("--search", help="General search keyword (looks in message or level)")
    parser.add_argument("--html", action="store_true", help="Export HTML report")
    parser.add_argument("--json", action="store_true", help="Export JSON report")
    parser.add_argument("--csv", action="store_true", help="Export CSV report")
    args = parser.parse_args()

    # Need to make sure we load config relative to where main is, or just from CWD
    # We'll assume the script is run from the root of the project
    config_path = "config.json"
    if not os.path.exists(config_path):
        # Fallback if run from src/
        config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    
    config = load_config(config_path)
    
    # Resolve project root to correctly place logs and reports
    project_root = os.path.dirname(os.path.abspath(config_path)) if os.path.exists(config_path) else os.getcwd()
    
    # Update config paths to be absolute based on project root
    if not os.path.isabs(config.get("log_file", "logs/application.log")):
        config["log_file"] = os.path.join(project_root, config.get("log_file", "logs/application.log"))
    if not os.path.isabs(config.get("output", "reports")):
        config["output"] = os.path.join(project_root, config.get("output", "reports"))

    logger = setup_app_logging(config)
    logger.info("Started analyzer")

    log_parser = LogParser(config["log_file"])
    logs = log_parser.parse()
    logger.info("Read file")

    analyzer = LogAnalyzer(logs, config)
    summary = analyzer.get_summary()

    exporter = Exporter(config["output"])

    search_keyword = args.contains or args.search
    if args.level or search_keyword or args.date:
        level_search = args.level
        if args.search and args.search.upper() in ["INFO", "WARNING", "ERROR"]:
            level_search = args.search.upper()
            search_keyword = None if not args.contains else args.contains
        
        results = analyzer.search(level=level_search, keyword=search_keyword, date=args.date)
        for log in results:
            print(f"{log['datetime']} - {log['level']} - {log['message']}")
        
        logger.info("Completed")
        return

    report_generated = False
    if args.html:
        exporter.export_html(summary)
        report_generated = True
    if args.json:
        exporter.export_json(summary)
        report_generated = True
    if args.csv:
        exporter.export_csv(summary)
        report_generated = True

    if report_generated:
        logger.info("Generated report")

    logger.info("Completed")
    
    if not any([args.html, args.json, args.csv, args.level, args.contains, args.date, args.search]):
        print("Log Analyzer completed successfully. No output flags provided.")
        print(f"Total Logs: {summary.get('total_logs', 0)}")
        print(f"Errors: {summary.get('error_count', 0)}")
        print(f"Warnings: {summary.get('warning_count', 0)}")
        print(f"Info: {summary.get('info_count', 0)}")

if __name__ == "__main__":
    main()
