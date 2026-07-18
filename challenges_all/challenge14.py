import requests
# Sends a GET request to:
# https://jsonplaceholder.typicode.com/users
# Print:
# Status code
# Number of users
# Print only the names using a list comprehension.

response = requests.get("https://jsonplaceholder.typicode.com/users")
rj = response.json()
names = [l["name"] for l in rj]
emails = [l["email"] for l in rj]
print(rj)
print(f"Status code {response.status_code}")
print(f"Number of users : {len(rj)}")
print(names)
print(emails)
