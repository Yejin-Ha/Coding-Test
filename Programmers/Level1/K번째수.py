def solution(array, commands):
    answer = []
    while commands:
        comm = commands.pop(0)
        string = [ array[idx] for idx in range(comm[0]-1, comm[1])]
        answer.append(sorted(string)[comm[2]-1])
    return answer

# 예제 코드 실행
print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
