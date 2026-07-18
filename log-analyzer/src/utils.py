import logging
import os
import json

def load_config(config_path="config.json"):
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {
        "log_file": "logs/application.log",
        "output": "reports",
        "top_errors": 5
    }

def setup_app_logging(config):
    log_file = config.get("log_file", "logs/application.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    logger = logging.getLogger("LogAnalyzer")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger
