num = int(input('숫자를 입력하세요: '))

def recur(x):
    if x < 1:
        return '0'
    elif x == 1:
        return '1'

    if (x % 2) == 0:
        return recur(int(x / 2)) + '0'
    else:
        return recur(int(x / 2)) + '1'

print(recur(num))
