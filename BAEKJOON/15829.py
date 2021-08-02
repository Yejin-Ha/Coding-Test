n = input()
input_str = input()
total = 0

for i in range(int(n)):
    num = ord(input_str[i]) - 96
    total += num * 31**(i)

print(total)
