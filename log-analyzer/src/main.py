def read_log(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print(f"failed to read data from {file_path} :: {e}")


# print(type(read_log("./log-analyzer/logs/application.log")))


def count_levels(data: list) -> dict:
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0,
              "UNKNOWN": 0, "TOTAL": len(data)}
    for log in data:
        parts = log.split()
        try:
            if parts[2] == "INFO":
                counts["INFO"] += 1
            elif parts[2] == "WARNING":
                counts["WARNING"] += 1
            elif parts[2] == "ERROR":
                counts["ERROR"] += 1
            else:
                counts["UNKNOWN"] += 1
        except IndexError:
            print("log level not found")
            counts["UNKNOWN"] += 1
    return counts


# print(count_levels(read_log("./log-analyzer/logs/application.log")))

def print_summary(counts: dict):
    print("========== Enterprise Log Analyzer ==========")
    print(f"\nTotal Lines : {counts["TOTAL"]}")
    print(f"\nINFO : {counts["INFO"]}")
    print(f"WARNING : {counts["WARNING"]}")
    print(f"ERROR : {counts["ERROR"]}")
    print(f"UNKNOWN : {counts["UNKNOWN"]}")


print_summary(count_levels(read_log("./log-analyzer/logs/application.log")))
