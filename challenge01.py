numbers = [1, 4, 6, 2, 7]

def challenge01(nums: list):
    
    avg = sum(nums) / len(nums) if nums else 0
    
    print(
        f"Numbers given: {nums}\n"
        f"Largest number from list: {max(nums)}\n"
        f"Smallest number from list: {min(nums)}\n"
        f"Sum of numbers: {sum(nums)}\n"
        f"Avg of numbers: {avg}"
    )

challenge01(numbers)