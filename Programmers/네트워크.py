'''
# 문제 풀이
- DFS 또는 BFS를 이용하여 푸는 문제이다.
- 무엇을 사용하던 상관이 없음
'''
def solution(n, computers):
    # 방문한 네트워크 확인을 위한 배열
    visited = [0] * n
    answer = 0

    while 0 in visited:
        for i in range(n):
            # 해당 네트워크에 방문하지 않았다면 다음이 실행된다.
            if visited[i] == 0:
                dfs(computers, visited, i)
                # 연결되어있는 네트워크가 존재 => answer에 1을 더함
                answer += 1

    return answer

def dfs(computers, visited, v):
    # 방문한 네트워크의 값 바꾸기
    if visited[v] == 0:
        visited[v] = 1

    for e in range(len(computers)):
        # 네트워크가 연결되어 있음 AND 네트워크에 방문하지 않음 => DFS 함수를 반복하여 방문했다는 표시를 생성 
        if computers[v][e] == 1 and visited[e] == 0:
            dfs(computers, visited, e)

