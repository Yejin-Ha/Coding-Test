''' 문제 풀이
# 입력 예제 
N = 10
n_list = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
M = 8
m_list = [10, 9, -5, 2, 3, 4, 5, -10]

# 분석
- N, n_list, M, m_list를 입력받는다.
case 1. result라는 빈 리스트를 생성한다.
    - for문을 이용하여 m_list의 각 원소에 접근한다.
    - filter(), len() 함수를 이용하여 n_list에 해당 원소와 같은 원소가 몇개인지 구한다.
    - 구한 값을 result 함수에 append 한다.

case 2. 길이가 M이고 값이 다 0인 result 리스트를 생성한다.
    - for문과 enumerate() 함수를 이용하여 m_list의 index와 value에 접근한다.
    - filter(), len() 함수를 이용하여 value와 같은 원소가 몇개가 있는지 구한다.
    - result의 index 자리의 값을 구한 값으로 바꾼다.  
'''
# case 1
def solution(N, n_list, M, m_list):
    result = []
    for v in m_list:
        result.append(len(list(filter(lambda x: x == v, n_list))))
    return result



# case 2
def solution(N, n_list, M, m_list):
    result = [0] * M
    for idx, v in enumerate(m_list):
        result[idx] = len(list(filter(lambda x: x == v, n_list)))
    return result
