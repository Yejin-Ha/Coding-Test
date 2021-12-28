def solution(citations):
    # 오름차순으로 정렬
    citations.sort()
    length = len(citations)
    
    for i in range(length):
        # 인용된 횟수가 남은 논문의 수 이상일 경우에 H-index의 최대값이 된다.
        if citations[i] >= length-i:
            return length - i
            
    # 조건에 맞는 수가 없다면 0을 반환한다.
    return 0
