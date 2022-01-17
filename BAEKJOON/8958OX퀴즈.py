N = int(input())
answers = []
for _ in range(N):
    answers.append(input())

for a in answers:
  score = 0
  sum = 0
  for i in a:
    if i == 'O':
      score += 1
      sum += score
    else:
      score = 0
  print(sum)
