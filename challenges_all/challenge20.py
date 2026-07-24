class ServerConnection:
    def __enter__(self):
        print("Connecting...")

    def __exit__(self, *args):
        print("Disconnecting...")


with ServerConnection():
    print("Checking server...")
