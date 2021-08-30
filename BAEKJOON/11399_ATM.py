'''
# ATM
- min_t를 사용하지 않아서 아쉽다.
'''
min_t = int(input())
times = input().split()
times = [int(t) for t in times]
times.sort()

result = 0
wait_time = 0
for t in times:
    wait_time += t
    result += wait_time

print(result)
