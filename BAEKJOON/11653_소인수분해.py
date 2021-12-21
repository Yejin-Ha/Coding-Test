# 입력받는 수
n = int(input())

# 소인수분해한 결과를 저장할 빈 배열
result = []

# n이 1보다 클 경우에만 반복한다.
while n > 1:
  # 2 ~ n+1의 범위에서 i가 n의 소인수라면 result에 i를 저장하고 n을 i로 나눈 값으로 변경한다.
  for i in range(2, n+1):
    if n % i == 0:
      result.append(i)
      n = int(n/i)
      break

for i in result:
  print(i)
