''' 풀이과정
# 문제 분석
문제에 나와있는 예시를 통해 이해를 하였다.
step1 - pop을 이용하여 truck_weights의 첫번째 데이터를 가져오고 b라는 변수에 저장한다.
step2 - b와 truck_weight의 첫번째 데이터를 더하여 weight보다 작거나 같은지 비교한다.
    - 작거나 같다면 a에 b의 값을 대입하고 b에는 truck_weight의 첫번째 데이터를 대입한다.
    - 크다면 a에 b의 값을 대입하고 b에는 0을 대입한다.
step3 - step2를 실행할 때 마다 answer에 1을 더한다.
step4 - 위의 과정을 반복하다가 truck_weight에 데이터가 존재하지 않는다면 실행을 끝낸다.
'''

# answer 1
# 총점 : 21.4 / 100.0
def solution(bridge_length, weight, truck_weights):
    a, b = 0, 0
    answer = bridge_length

    while True:
        if b + truck_weights[0] <= weight:
            a, b = b,truck_weights.pop(0)
            answer += 1
        else:
            a, b = b, 0
            answer += 1

        if not truck_weights: 
            break
    return answer


# answer 2
# 총점 : 100.0 / 100.0
def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    
    while q: 
        time += 1
        q.pop(0) 

        if truck_weights: 
            if sum(q) + truck_weights[0] <= weight: 
                q.append(truck_weights.pop(0)) 
            else:
                q.append(0) 
    return time
