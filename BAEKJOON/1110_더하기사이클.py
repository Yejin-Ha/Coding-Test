n = int(input())

k = n
count = 1

while True:
  # 숫자의 10의 자리와 1의 자리를 더하고 그 수의 1의 자리를 x로 설정한다.
  x = (k // 10 + k % 10) % 10
  # 숫자의 1의 자리와 x를 통해 새로운 숫자를 만든다.
  y = (k % 10) * 10 + x

  # 새로운 숫자가 입력받은 숫자와 동일하면 while문을 종료한다.
  if n == y:
    break
  else:
    k = y
    count += 1

print(count)
