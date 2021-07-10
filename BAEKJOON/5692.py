"""
# 풀이과정
step01 - 각 자릿수를 10의 n승으로 나눠가며 몫이 0이 아니라면 n!를 몫과 곱하여 num이라는 변수에 더해준다.
step02 - 입력받은 숫자마다 위의 과정을 반복해간다.
step03 - 입력받은 데이터의 마지막은 0이므로 무시한다.

# 코드 설명
inputs : 페이지에 나와있는 입력된 예제
lst : 10의 n승의 데이터가 담겨있는 배열
"""

inputs = [719, 1, 15, 110, 102, 0]
lst = [10000, 1000, 100, 10, 1]

for input in inputs[:-1]:
    num = 0
    n = input

    for i in lst:
        x = n // i

        if x != 0:
            n = n - x * i
            y = len(lst) - lst.index(i)
            factorial = 1

            for j in range(1, y+1):
                factorial *= j
            num += (x * factorial)

    print(input, num)
