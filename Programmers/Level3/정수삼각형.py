"""
상단의 숫자 중 큰 숫자를 하단으로 더해간다.
하단의 숫자 중 최대값을 결과로 반환한다.
"""
def solution(tri):
    for i in range(1, len(tri)):
        # 배열의 처음과 끝은 상단에 비교할 숫자가 없기 때문에 바로 더한다.
        tri[i][0] += tri[i-1][0]
        tri[i][len(tri[i])-1] += tri[i-1][len(tri[i-1])-1]

        for j in range(1, len(tri[i])-1):
            if tri[i-1][j-1] >= tri[i-1][j]:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += tri[i-1][j]
    return max(tri[-1])
  
