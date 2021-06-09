''' 풀이과정
# 문제 분석


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
