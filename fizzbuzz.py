nums = []

for x in range(0,101):
    nums.append(x)

for x in range(0, len(nums), 3):
    nums[x] = "Fizz"

for x in range(0, len(nums), 5):
    nums[x] = "Buzz"

for x in range(0, len(nums), 15):
    nums[x] = "FizzBuzz"

for x in nums:
    print(x)