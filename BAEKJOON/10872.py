'''
# 문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''
# 2021/08/05 풀이
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return n * factorial(n-1)

num = int(input("숫자를 입력하세요: "))

print(factorial(num))

# 2021/12/23 풀이
def solution(n):
  if n < 2:
    return 1
  else:
    return n * solution(n-1)

if __name__ == '__main__':
  n = int(input())
  print(solution(n))
