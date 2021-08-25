'''
# 주유소
'''

# city_num = int(input())
lengths = input().split()
citys = input().split()

ass =0

cost = int(citys[0]) * int(lengths[0])
print(int(citys[citys.index(min(citys[:-1]))]))
# [int(n) for n in lengths[citys.index(min(citys)):-1]]
# print(lengths[citys.index(min(citys))])
print(sum([int(n) for n in lengths[citys.index(min(citys))-2:]]


# cost += int(citys[citys.index(min(citys))-1]) * sum(int(lengths[citys.index(min(citys))-1:-1]))