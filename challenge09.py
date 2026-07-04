import json


def analyze_servers(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        healthy_count = 0
        down_count = 0
        high_cpu_list = []
        scanned_servers = []

        for line in data:
            line.pop("ip")
            scanned_servers.append(line)
            if line["status"] == "Healthy":
                healthy_count += 1
            elif line["status"] == "Down":
                down_count += 1
        for line in data:
            if line["cpu"] >= 80:
                host = f"{line["hostname"]} {line["cpu"]}"
                high_cpu_list.append(host)
    status = {
        "Healthy Servers": healthy_count,
        "Down Servers": down_count
    }
    return scanned_servers, status, high_cpu_list


print(analyze_servers("json//server_status.json"))
servers, status_summary, high_cpu = analyze_servers("json//server_status.json")

print("========= Server Health Report =========")
for server in servers:
    print(f"Hostname : {server["hostname"]}")
    print(f"Status : {server["status"]}")
    print(f"CPU : {server["cpu"]}\n")
print("-" * 30)
print(f"Healthy Servers : {status_summary["Healthy Servers"]}")
print(f"Down Servers    : {status_summary["Down Servers"]}\n")
print("-" * 30)
print("High CPU Servers (>80%)\n")
for server in high_cpu:
    print(server)


#################################################################


def analyze_servers(filename: str):
    """
    Read server information from a JSON file and generate a health summary.

    Args:
        filename: Path to the JSON file.

    Returns:
        Tuple containing:
        - List of servers
        - Summary dictionary
        - List of high CPU servers
    """

    with open(filename, "r") as file:
        servers = json.load(file)

    healthy_count = 0
    down_count = 0
    high_cpu_servers = []

    # Process every server only once
    for server in servers:

        if server["status"] == "Healthy":
            healthy_count += 1

        elif server["status"] == "Down":
            down_count += 1

        if server["cpu"] > 80:
            high_cpu_servers.append(server)

    summary = {
        "Healthy Servers": healthy_count,
        "Down Servers": down_count,
    }

    return servers, summary, high_cpu_servers


# --------------------------
# Main Program
# --------------------------

servers, summary, high_cpu = analyze_servers("json/server_status.json")

print("=" * 40)
print("Server Health Report")
print("=" * 40)

for server in servers:
    print(f"Hostname : {server['hostname']}")
    print(f"IP       : {server['ip']}")
    print(f"Status   : {server['status']}")
    print(f"CPU      : {server['cpu']}%")
    print("-" * 40)

print(f"Healthy Servers : {summary['Healthy Servers']}")
print(f"Down Servers    : {summary['Down Servers']}")

print("\nHigh CPU Servers (>80%)")

for server in high_cpu:
    print(f"{server['hostname']} ({server['cpu']}%)")
