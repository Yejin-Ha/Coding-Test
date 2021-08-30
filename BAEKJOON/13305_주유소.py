'''
# 주유소
'''
city_num = int(input()) - 2
lengths = input().split()
citys = input().split()
result = 0

cost = int(citys.pop(0))
street = int(lengths.pop(0))

# 맨 마지막 주유소와 시작 주유소는 비교할 필요가 없어서 2를 뺀다.
while city_num:
    # 다음 주유소가 싸다 => 멈추기
    if cost > int(citys[0]):
        result += cost * street
        cost = int(citys.pop(0))
        street = int(lengths.pop(0))
    # 다음 주유소가 비싸다 => 계속 진행
    else:
        citys.pop(0)
        street += int(lengths.pop(0))

    city_num -= 1

result += cost * street
print(result)
