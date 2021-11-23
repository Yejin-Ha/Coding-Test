a = list(map(int, input().split(' ')))
n_list = list(map(int, input().split(' ')))
result = []

for i in range(0, a[0]):
    if a[1] > n_list[i]:
        result.append(n_list[i])

print(' '.join(map(str, result)))