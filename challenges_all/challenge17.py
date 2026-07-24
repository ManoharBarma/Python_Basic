def check_services(*services):
    for service in services:
        print(service)


def create_vm(**config):
    for key, value in config.items():
        print(f"{key} : {value}")


create_vm(
    name="web01",
    cpu=4,
    memory=8,
    os="ubuntu",
    region="eastus",
    disk=100,
    backup=True
)
