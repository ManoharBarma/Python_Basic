employee = {
    "name": "Barma",
    "role": "DevOps Engineer",
    "experience": 3
}

print(employee["name"])
print(employee["role"])
print(employee["experience"])

server = {
    "hostname": "web01",
    "ip": "10.0.0.5",
    "status": "Healthy"
}

print(f'Hostname: {server["hostname"]}')
print(f'IP: {server["ip"]}')
print(f'Status: {server["status"]}')

servers = [{
    "hostname": "web01",
    "status": "Healthy"
},
    {
    "hostname": "web02",
    "status": "Down"
},
    {
    "hostname": "db01",
    "status": "Healthy"
}]
count = 0
for server in servers:

    print(f'{server["hostname"]} -> {server["status"]}')
    if server["status"].lower() == "healthy":
        count += 1
print(f'Healthy Servers = {count}')


def find_server(my_server: str, servers: dict):
    server_status = False
    for server in servers:
        if server["hostname"].lower() == my_server.lower():
            server_status = True
            break
    print("server found") if server_status else print("server not found")

find_server("db01", servers)
