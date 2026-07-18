list1 = [{
    "name": "Person A",
    "company": {
        "name": "Company X"
    }
}]
# Person A --> Company X
emps = [f'{l["name"]} --> {l["company"]["name"]}' for l in list1]
print(emps)
