import sys

# 입력받은 숫자들의 중복되지 않은 나머지를 담을 배열
result = []

for i in range(10):
  n = int(sys.stdin.readline())
  remainder = n % 42
  # 나머지가 result 배열에 없다면 추가한다
  if remainder not in result:
    result.append(remainder)

print(len(result))
