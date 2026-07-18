import re
# text = "Server status: Running"
#
# result = re.search("Running", text)
#
# print(result)

text = "Server1 Server22 Server333"

results = re.findall(r"\d+", text)

print(results)

text2 = "INFO ERROR INFO ERROR WARNING ERROR"
print(len(re.findall("ERROR", text2)))

logs = """
INFO Application started
ERROR Database timeout
INFO User login
ERROR Disk full
WARNING CPU usage high
"""

errors = re.findall(r"^ERROR.*", logs, re.MULTILINE)
for error in errors:
    print(error)
