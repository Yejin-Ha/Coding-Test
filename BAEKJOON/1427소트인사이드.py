N = input()
num = []

for n in N:
  num.append(int(n))

while num:
  # 배열의 원소 중 가장 큰 값만 출력&제거
  max_n = max(num)
  print(max_n, end='')
  num.remove(max_n)
  
