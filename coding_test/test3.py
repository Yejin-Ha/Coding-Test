candles = [2,2,2,4]
lights = [candles.pop(0)]
result = 0

while True:
    result += 1

    for idx in range(0, len(lights)):
        lights[idx] -= 1  

    while 0 in lights:
        lights.remove(0)

    if len(candles):
        lights.append(candles.pop(0))
    print(candles, lights)

    if len(candles) == 0 and len(lights) == 0:
        print(candles, lights)
        break

print(result)    


# for idx in range(0, len(ass)):
#     ass[idx] -= 1

# print(ass)
# while 0 in ass:
#     ass.remove(0)
# print(ass)