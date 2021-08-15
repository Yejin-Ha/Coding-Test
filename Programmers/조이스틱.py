def solution(name):
    moves = [min(ord(x)-ord('A'), ord('Z')-ord(x)+1) for x in name]
    idx = 0
    answer = 0

    while True:
        answer = answer + moves[idx]
        moves[idx] = 0

        if sum(moves) == 0:
            return answer

        left, right = 1, 1
        while moves[idx - left] == 0:
            left += 1
        while moves[idx + right] == 0:
            right += 1
        
        answer += left if left < right else right
        idx += -left if left < right else right


print(solution("JAN"))
dho dksehlwl