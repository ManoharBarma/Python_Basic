from pathlib import Path
import os


print(os.getcwd())
print(os.listdir())

count = 0
for file in os.listdir():
    if file.endswith(".py"):
        print(file)
        count += 1
print(f"Total Python files: {count}")


#  Using only pathlib, write a program that:
#  Prints the current directory.
#  Lists all files.
#  Prints only .json files.
#  Counts how many .json files exist.
#  Prints:
#  Total JSON files: X
count2 = 0
print(Path.cwd())
os.chdir(Path("json"))
files = Path.cwd().iterdir()
print(files)
for file in files:
    if file.suffix == ".json":
        print(file)
        count2 += 1

print(count2)
