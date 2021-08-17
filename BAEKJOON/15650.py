'''
# 문제 풀이 힌트
- 깊이 우선 탐색(DFS)을 활용한다.
'''

# 자연수 N, M을 입력받는다.
n,m = list(map(int,input().split()))
# 반환할 결과 리스트
result = []

# 깊이 우선 탐색 함수 생성(매개변수로는 탐색을 시작할 숫자를 입력받는다.)
def dfs(start):
    # 결과(result)의 길이가 입력된 길이와 같다면 탐색을 멈추고 결과를 출력한다.
    if len(result)==m:
        print(' '.join(map(str, result)))
        return
    
    # 반복문을 사용하여 수열 생성(시작할 숫자 ~ 입력받은 숫자)
    for i in range(start, n+1):
        # i가 결과에 포함되지 않는다면 결과에 포함하고 깊이우선 탐색을 통해 수열을 생성한다.
        if i not in result:
            result.append(i)
            # 재귀함수를 통해 반복문이 중첩되는 것을 활용한다.
            dfs(i+1)
            result.pop()

dfs(1)
