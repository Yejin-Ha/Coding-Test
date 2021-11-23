times = input()
times = list(map(int, times.split(' ')))

if times[1] < 45:
    times[0] -= 1
    times[1] += 15
else:
    times[1] -= 45

if times[0] < 0:
    times[0] = 24 + times[0]

print(' '.join(map(str, times)))
