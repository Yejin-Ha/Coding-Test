''' 문제 풀이
# 문제 분석
step01 - n을 입력받는다.
step02 - 1부터 n까지의 정수로 이루어진 deque를 생성한다.
step03 - deque에 데이터가 존재한다면 popleft와 append를 통해 deque의 첫번째 데이터를 res에 넣는다.
step04 - deque의 메소드 중 rotate를 이용하여 맨 마지막 데이터를 맨 처음으로 옮긴다.
step05 - step03 ~ step04를 반복한다.
step06 - deque에 데이터가 존재하지 않는다면 실행을 멈추고 res를 반환한다.
'''
# answer 1
from collections import deque
n = int(input())
res = []
que = deque(list(range(1, n+1)))
while True:
    if que:
        res.append(que.popleft())
        que.rotate(-1)
    else:
        break

print(res)

# answer 2
n = int(input())
cards = list(range(1, n+1))
res = []
while len(cards) > 1:
    res.append(cards[0])
    cards = cards[2:]+[cards[1]]
res.append(cards[0])

print(*res)
