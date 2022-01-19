T = int(input())

p = []
for _ in range(T):
  k = int(input())
  n = int(input())
  if k == 1:
    p.append([i for i in range(1, n+1)])
  else:
    k_p = []
    sum = 0
    for i in range(n):
      sum += p[k-2][i]
      k_p.append(sum)
    p.append(k_p)

for i in p:
  sum = 0
  for n in i:
    sum += n
  print(sum)
