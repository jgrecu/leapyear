def high_and_low(numbers):
    nums = [int(i) for i in numbers.split()]
    return f"{max(nums)} {min(nums)}"

print(high_and_low("1 2 3 4 5 -1"))
print(high_and_low("1 2 -3 4 5"))
print(high_and_low("1 9 3 4 -5"))
print(high_and_low("1 2 0 -2 5 -9"))
