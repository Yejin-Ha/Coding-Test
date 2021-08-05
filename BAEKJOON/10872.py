'''
# 문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return n * factorial(n-1)

num = int(input("숫자를 입력하세요: "))

print(factorial(num))
