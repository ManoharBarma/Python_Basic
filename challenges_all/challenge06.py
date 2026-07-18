servers = [
    {"hostname": "web01", "status": "Healthy"},
    {"hostname": "web02", "status": "Down"},
    {"hostname": "db01", "status": "Healthy"},
    {"hostname": "app01", "status": "Down"},
    {"hostname": "app02", "status": "Healthy"},
    {"hostname": "app420", "status": "dhHealthy"}
]

healthy_count = 0
down_count = 0
for server in servers:
    if server["status"].lower() == "healthy":
        healthy_count += 1
    elif server["status"].lower() == "down":
        down_count += 1
        print(f'{server["hostname"]} is Down')
    else:
        print(
            f'Host {server["hostname"]} status is unknow ({server["status"]})')
print(f'Healty = {healthy_count}\nDown = {down_count}')


def server_report(servers: list):
    print("--------------------------------")
    for server in servers:
        print(f'''Hostname : {server["hostname"]}
Status   : {server["status"]} 
--------------------------------''')


server_report(servers)
