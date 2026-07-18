pods = [
    {"name": "frontend", "ready": "1/1", "status": "Running"},
    {"name": "backend", "ready": "1/1", "status": "Running"},
    {"name": "redis", "ready": "0/1", "status": "Pending"},
    {"name": "mongodb", "ready": "0/1", "status": "CrashLoopBackOff"},
    {"name": "nginx", "ready": "1/1", "status": "Running"},
]

# Use one list comprehension
# Don't use a normal for loop for filtering
# Use an f-string
# Don't modify the original list

# po = [
#     f"{pod["name"]} --> {pod["status"]}" for pod in pods if pod["status"] != "Running"
# ]
# print(po)
# Healthy Pods : 3
# Unhealthy Pods : 2

Healthy_count = 0
Unhealthy_count = 0
for pod in pods:
    if pod["status"] == "Running":
        Healthy_count += 1
    else:
        Unhealthy_count += 1

print(f"Healthy Pods : {Healthy_count}")
print(f"Unhealthy Pods : {Unhealthy_count}")
