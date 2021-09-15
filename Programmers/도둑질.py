'''
# 입출력 예
    money   	return
[1, 2, 3, 1]	4

# 문제 포인트
첫번째 집을 무조건 터는 경우와 마지막 집을 무조건 터는 경우로 구분한다.
(인접한 두 집을 털면 경보가 울리기 때문에 두 집을 한번에 터는 경우는 없다.)
'''

def solution(money):
    # 첫번째 집을 터는 경우의 list
    table_start = [0] * (len(money) - 1)  # 마지막 집을 털지 않으니 money list보다 크기가 1 작은 list로 만든다.
    table_start[0] = money[0]
    table_start[1] = table_start[0]  # 첫번째 집을 털었으니 두번째 집은 털지 않아서 돈이 그대로다.

    # 마지막 집을 털지 않으니 money list의 마지막 element는 확인할 필요가 없다. => len(money)-1
    for i in range(2, len(money) - 1):
        # 현재의 집을 털지 않고 넘어갈 경우와 현재 집을 털 경우 중 돈이 더 많은 경우를 채택한다.
        table_start[i] = max(table_start[i-1], table_start[i-2]+money[i])

    # 마지막 집을 터는 경우의 list
    table_end = [0] * len(money)
    table_end[1] = money[1]  

    for i in range(2, len(money)):
        # 현재의 집을 털지 않고 넘어갈 경우와 현재 집을 털 경우 중 돈이 더 많은 경우를 채택한다.
        table_end[i] = max(table_end[i-1], table_end[i-2]+money[i])
        
    # 두 table의 최고값 중 최고값을 반환한다.
    return max(max(table_start), max(table_end))
    