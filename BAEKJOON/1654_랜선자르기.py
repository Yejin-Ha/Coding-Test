'''
# 랜선 자르기
- 이진탐색 알고리즘 활용
'''
# 입력받는 정보들
num, max_len = map(int, input().split())
lengths = []

for _ in range(num):
    lengths.append(int(input()))

# 시작 길이: 1, 끝 길이: 제일 긴 랜선의 길이
start_len = 1
end_len = max(lengths)

# 이진탐색중 시작 길이가 끝 길이보다 크면 안된다.
while (start_len <= end_len):
    # 시작과 끝의 중앙값을 통해 이진탐색을 한다.
    mid = (start_len + end_len) // 2
    
    # 중앙값으로 랜선을 자르는 경우의 생기는 개수
    counts = 0
    counts = sum([length // mid for length in lengths])

    # 이진탐색 
    if counts >= max_len:
        start_len = mid + 1
    else:
        end_len = mid - 1

print(end_len)
