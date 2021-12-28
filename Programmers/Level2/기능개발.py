''' 풀이과정
# 분석
step 1. 각 progresses의 데이터에 각 speeds 데이터를 더한다.
step 2. if 맨 처음의 데이터가 100보다 크거나 같을 경우 -> 다음 인덱스의 데이터도 100보다 크거나 같은지 비교한다.
    step 2-1. if 다음 인덱스의 데이터가 100보다 크거나 같을 경우
        - step 2를 반복한다. 
    step 2-2. if 다음 인덱스의 데이터가 100보다 작을 경우 
        - step 1을 반복한다.
step 3. if 맨 처음의 데이터가 100보다 작을 경우
    - step 1을 반복한다.

# solution() 참고
check : list type, progresses의 같은 길이이며 모든 값이 False이다. 
    * False만 들어있는 check list를 만들어서 progresses의 데이터가 100보다 크거나 같으면 해당 인덱스의 값을 True로 변경했다.
count : int type, 100보다 크거나 같은 데이터의 수를 의미한다.
    * answer.append(count)를 통해 구한 결과를 answer 큐에 저장했다.
'''


def solution(progresses, speeds):
    answer = []
    check = [False] * len(progresses)
    
    while True:    
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        for i in range(check.index(False), len(progresses)):
            count = 0
            if progresses[i] >= 100:
                count += 1
                check[i] = True
            else:
                break

        if count != 0:
            answer.append(count)

        if False not in check:
            break       
    return answer


''' 채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''
