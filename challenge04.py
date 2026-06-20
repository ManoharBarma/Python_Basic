def challenge04(numbers: list, target: int):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count

numbers = [10, 20, 10, 30, 10, 40]
target = 10
print(challenge04(numbers, target))