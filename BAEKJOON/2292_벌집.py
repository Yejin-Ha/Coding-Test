# 첫번째 시도
def solution1(n):
  # 입력받은 수가 1~8라면 다음을 반환
  if n == 1:
    return 1
  elif n < 8:
    return 2

  count = 1
  while n > 0:
    k = 6 * count
    n -= k
    count += 1

  return count
  # 결과는 실패
    
# 두번째 시도
def solution2(n):
  # 벌집 수를 k로 지정
  k = 1
  count = 1

  # 벌집은 6의 배수로 커지는 것을 참고
  while n > k:
    k += 6 * count
    count += 1

  return count
  # 결과는 성공
