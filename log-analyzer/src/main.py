import re


def read_log(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print(f"failed to read data from {file_path} :: {e}")
    return data


# print(read_log("./log-analyzer/logs/application.log"))


def count_levels(data: list(str)) -> dict:
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0,
              "UNKNOWN": 0, "TOTAL": len(data)}
    for log in data:
        log_split = log.split()
        if log_split[2] == "INFO":
            counts["INFO"] += 1
        elif log_split[2] == "WARNING":
            counts["WARNING"] += 1
        elif log_split[2] == "ERROR":
            counts["ERROR"] += 1
        else:
            counts["UNKNOWN"] += 1
    return counts


# print(count_levels(read_log("./log-analyzer/logs/application.log")))

def print_summary(count_levels: dict):
    print("========== Enterprise Log Analyzer ==========")
    print(f"\nTotal Lines : {count_levels["TOTAL"]}")
    print(f"\nINFO : {count_levels["INFO"]}")
    print(f"WARNING : {count_levels["WARNING"]}")
    print(f"ERROR : {count_levels["ERROR"]}")
    print(f"UNKNOWN : {count_levels["UNKNOWN"]}")


print_summary(count_levels(read_log("./log-analyzer/logs/application.log")))
