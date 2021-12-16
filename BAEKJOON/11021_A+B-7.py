n = int(input())
for i in range(0, n):
  nums = list(map(int, input().split(' ')))
  print(f'Case #{i+1}: {nums[0] + nums[1]}')
