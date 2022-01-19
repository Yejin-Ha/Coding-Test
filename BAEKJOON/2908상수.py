nums = list(input().split(' '))

for i in range(len(nums)):
  nums[i] = nums[i][::-1]

print(max(nums))
