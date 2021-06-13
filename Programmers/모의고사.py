''' 풀이과정
# 분석
- 각 수포자들을 p1, p2, p3의 리스트로 구성한다.
    - p1, p2, p3의 리스트에는 순환되는 찍는 번호들을 입력한다.
- 입력받은 answers 리스트와 수포자들의 리스트를 비교하여 같은 위치에 value가 같다면 점수를 1점씩 준다.
    - enumerate() 함수를 사용하여 answers 리스트의 각 index와 value에 접근할 수 있도록 한다.
    - %(나머지를 반환하는 연산기호)를 이용하여 수포자들의 리스트가 순환되도록 한다.
    - 정답이 일치할 경우 scores 리스트에 1점씩 더한다.
- 가장 많이 맞힌 사람을 찾는다.
    - scores의 최대값의 위치(index)를 max() 함수를 통하여 구하고 result 리스트에 해당하는 수포자의 번호를 추가(append)한다.
'''

def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores, result = [0, 0, 0], []
    
    for idx, answer in enumerate(answers):
        if answer == p1[idx % len(p1)]:
            scores[0] += 1
        if answer == p2[idx % len(p2)]:
            scores[1] += 1
        if answer == p3[idx % len(p3)]:
            scores[2] += 1
        
    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx + 1)
            
    return result

'''
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''