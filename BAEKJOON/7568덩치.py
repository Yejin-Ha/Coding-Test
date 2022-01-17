N = int(input())
p = []
for _ in range(N):
    w, l = map(int, input().split(' '))
    p.append([w, l])

for i in p:
    rank = 1
    for j in p:
        # i학생이 j학생보다 덩치가 작을 경우에만 rank를 더한다. => 
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=' ')
