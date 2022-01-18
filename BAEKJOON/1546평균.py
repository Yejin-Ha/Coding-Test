N = int(input())
scores = list(map(int, input().split(' ')))

M = max(scores)
new_scores = []
for scr in scores:
  new_scores.append(scr/M*100)
print(sum(new_scores)/N)
