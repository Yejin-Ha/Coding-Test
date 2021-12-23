n = int(input())

# 결과를 담을 1차원 배열
result = []

# 입력된 숫자만큼 반복
for _ in range(0, n):
  a, b = map(int, input().split(' '))
  c = a + b
  result.append([a, b, c])

for i in range(0, n):
  print(f'Case #{i+1}: {result[i][0]} + {result[i][1]} = {result[i][2]}')
