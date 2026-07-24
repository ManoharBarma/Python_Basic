def logger(func):
    def wrapper():
        print("===== LOG START =====")
        func()
        print("===== LOG START =====")
    return wrapper


@logger
def delete_pod():
    print("Deleting pod...")


delete_pod()
