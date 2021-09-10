from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            # sorted(order)의 문자들 중 c개로 이루어진 조합 전체를 찾는다.
            combi = combinations(sorted(order), c)
            temp += combi

        # Counter 메소드를 이용하여 각 문자가 전체에서 몇개 존재하는지 count 한다.
        counter = Counter(temp)

        # 조합이 존재하고 조합의 개수의 최고값이 1보다 크다면
        if len(counter) != 0 and max(counter.values()) > 1:
            # count가 최고값인 조합을 정답에 추가한다.
            answer += [''.join(x) for x in counter if counter[x] == max(counter.values())]

            # 식 단순화 하기
            # for x in counter:
            #     if counter[x] == max(counter.values()):
            #         answer += [''.join(x)]

    return sorted(answer)
