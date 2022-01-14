# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary_num = ''

    while N > 1:
        binary_num = str(N%2) + binary_num
        N = N//2
    binary_num = '1' + binary_num

    if binary_num.count('1') < 2:
        return 0
    else:
        binary_gap = [0] * (binary_num.count('1')-1)
        cnt = 0
        for i in binary_num[1:]:
            if i == '1':
                cnt += 1
            else:
                binary_gap[cnt] += 1
        return max(binary_gap)
