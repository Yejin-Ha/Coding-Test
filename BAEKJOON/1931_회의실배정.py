'''
# 회의실 배정
'''
n = int(input())
times = []
for _ in range(n):
    [start, end] = input().split()
    times.append([int(start), int(end)])

# 끝나는 시간을 기준으로 오름차순 정렬하고 중복시 시작 시간을 기준으로 오름차순 정렬한다.
    # 빨리 끝날수록 다른 회의가 시작될 기회가 많아서 끝나는 시간이 빠른 순으로 정렬한다.
sort_times = sorted(times, key=lambda x: (x[1], x[0]))


end_t = 0
result = 0

for x, y in sort_times:
    # 시작 시간(x)가 전 회의가 끝나는 시간(end_t)보다 크거나 같다면 회의를 시작할 수 있다.
    if x >= end_t:
        # 새로운 회의가 시작했으니 end_t를 바꾼다.
        end_t = y
        result += 1

print(result)
