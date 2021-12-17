def solution(n):
  # 99 이하의 모든 숫자들은 한수이다.
  if n < 100:
    return n
    
  # 100 이상의 숫자들 중 한수 찾기
  else:
    result = 99
    for i in range(100, n+1):   
      nums = list(map(int, str(i)))
      if nums[0] - nums[1] == nums[1] - nums[2]:
        result += 1
    return result
    
if __name__ == "__main__":
  n = int(input())
  print(solution(n))
