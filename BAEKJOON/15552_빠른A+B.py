# sys.stdin.readline()을 사용하기위해 모듈 import
import sys

n = int(input())

# 두 수를 더한 값들을 담을 배열
result = []

for i in range(n):
  # \n을 기준으로 문자열을 구분한다.
  nums = sys.stdin.readline().strip()
  a, b = map(int, nums.split(' '))
  result.append(a+b)

for i in result:
  print(i)
