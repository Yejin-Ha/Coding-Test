n_list = []

while True:
    n = list(map(int, input().split(' ')))
    if n[0] == 0 & n[1] == 0:
        break
    else:
        n_list.append(n)

for i in range(0, len(n_list)):
    print(n_list[i][0] + n_list[i][1])