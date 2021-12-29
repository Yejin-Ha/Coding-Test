def solution(lottos, win_nums):
    # lottos와 win_nums 집합의 교집합의 개수 구하기
    count = len(set(lottos) & set(win_nums))
    
    # lottos에서 0의 개수 구하기
    zeros = lottos.count(0)
    
    return [7-max(1, count+zeros), 7 - max(1, count)]
