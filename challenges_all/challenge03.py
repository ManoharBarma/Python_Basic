numbers = [10, 50, 20, 80, 30]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num < largest:
        second_largest = num


print(f'largest: {largest} and second largest: {second_largest}')
