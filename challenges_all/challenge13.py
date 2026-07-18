import subprocess

git = subprocess.run(["git", "--version"], capture_output=True, text=True)

if git.returncode == 0:
    print("Git is installed.")
    print(git.stdout)
else:
    print("Git is not installed.")


try:
    k8s = subprocess.run(
        ["kubectl", "version", "--client"],
        capture_output=True,
        text=True
    )

    if k8s.returncode == 0:
        print("Kubectl installed.")
        print(k8s.stdout)
    else:
        print("Kubectl command failed.")
        print(k8s.stderr)

except FileNotFoundError:
    print("Kubectl is not installed or not in PATH.")
