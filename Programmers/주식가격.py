''' 풀이 과정
# 분석 
입출력 예를 보고 다음을 생각했다.
    prices[0] = 1 -> 나머지 4개의 값보다 작다.
    prices[1] = 2 -> [1]을 제외한 나머지 3개의 값보다 작다.
    prices[2] = 3 -> [1, 2]를 제외한 나머지 중 2보다는 크고 3과는 같다.
    prices[3] = 2 -> [1, 2, 3]을 제외한 나머지 1개의 값보다 작다.
    prices[4] = 3 -> [1, 2, 3, 2]를 제외하고 비교할 나머지 값이 없다.

즉, 이전의 데이터를 제외하고 뒤에 있는 데이터들과 비교했을 때 같거나 작은 수만큼 +1을 하면 [4, 3, 1, 1, 0]을 구할 수 있다.
'''

def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
    return answer

