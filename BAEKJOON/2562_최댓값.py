n_list = []
for _ in range(0, 9):
  n_list.append(int(input()))

n_max = max(n_list)

print(n_max)
print(n_list.index(n_max)+1)
