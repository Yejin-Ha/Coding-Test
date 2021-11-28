n = int(input())
cases = []

for i in range(0, n):
    a = list(map(int, input().split(' ')))
    cases.append(a)

for i in range(0, n):
    print(cases[i][0]+cases[i][1])