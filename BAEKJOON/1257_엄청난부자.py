money = int(input())
coin_type = int(input())
coins = [int(coin) for coin in input().split(' ')]
coins.sort(reverse=True)

answer = 0

for coin in coins:
    answer += money // coin
    money = money % coin

print(answer)
