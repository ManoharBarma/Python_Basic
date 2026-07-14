servers = [
    {"name": "app1", "cpu": 45},
    {"name": "app2", "cpu": 90},
    {"name": "db1", "cpu": 81},
    {"name": "cache1", "cpu": 35},
]

server_names = [
    server["name"]
    for server in servers
    if server["cpu"] > 80
]

print(server_names)


servers2 = [
    {"name": "app1", "status": "Healthy", "cpu": 35},
    {"name": "app2", "status": "Down", "cpu": 90},
    {"name": "db1", "status": "Healthy", "cpu": 82},
    {"name": "cache1", "status": "Healthy", "cpu": 95},
]

server_names2 = [
    server["name"] for server in servers2 if server["status"] == "Healthy" and server["cpu"] > 80
]

print(server_names2)

servers3 = [
    {"name": "app1", "status": "Healthy", "cpu": 35},
    {"name": "app2", "status": "Down", "cpu": 90},
    {"name": "db1", "status": "Healthy", "cpu": 82},
]

server_names3 = [{"name": server["name"], "cpu": server["cpu"]}
                 for server in servers3]

print(server_names3)

instances = [
    {"id": "i-101", "state": "running", "type": "t2.micro"},
    {"id": "i-102", "state": "stopped", "type": "t3.medium"},
    {"id": "i-103", "state": "running", "type": "t3.large"},
    {"id": "i-104", "state": "terminated", "type": "t2.micro"},
]

instances_out = [
    f"{inst["id"]} ({inst["type"]})"
    for inst in instances
    if inst["state"] == "running"
]

print(instances_out)

pods = [
    {"name": "frontend", "namespace": "prod"},
    {"name": "backend", "namespace": "prod"},
    {"name": "redis", "namespace": "cache"},
]

pods_out = [
    f"{po["namespace"]}/{po["name"]}" for po in pods
]

print(pods_out)
