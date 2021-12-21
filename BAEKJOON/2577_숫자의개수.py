A = int(input())
B = int(input())
C = int(input())

num = str(A * B * C)
result = [0] * 10

for i in range(0, 10):
  result[i] = num.count(str(i))

for i in result:
  print(i)
