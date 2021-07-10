'''
# 풀이 과정
step01 - 입력받은 문자열 중 첫번째 문자부터 접근을 한다.
step02 - 숫자가 아니라면 아스키코드로 변경한 뒤 55를 빼서 각 알파벳의 숫자를 정리해준다.
step03 - 문자를 정해진 숫자로 변경한 뒤 주어진 진법을 곱하고 다음 문자의 수를 더한다.
step04 - 위의 과정을 반복하여 입력된 문자열을 10진법으로 변경한다.

# 코드 설명
inputs : 문제 페이지에 주어진 예제
num : 입력된 문자열을 10진법으로 변경한 숫자
'''

inputs = ['ZZZZZ', 36]

if not inputs[0][0].isdigit():
    x = ord(inputs[0][0]) - 55
else:
    x = int(inputs[0][0])

num = x

print(num)


for i in inputs[0][1:]:
    if not i.isdigit():
        i = ord(i) - 55
    else:
        i = int(i)

    num *= inputs[1]
    print(num)
    num += i
    print(num)
    print('--'*20)
