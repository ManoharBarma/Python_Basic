def challenge02(numbers: list):
    if not numbers:
        print("List is empty")
        return
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    print(f'largest: {largest} and smallest: {smallest}')

challenge02([453,64325,254352,6256,34223])