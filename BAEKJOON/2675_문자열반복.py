n = int(input())

# 결과를 담을 result 배열
result = []

# 입력받은 n만큼 수행한다.
for _ in range(0, n):
  # ' '를 구분으로 반복할 횟수(r), 문자열(s)를 입력받는다.
  r, s = input().split(' ')
  r = int(r)
  
  # s를 r번 반복한 결과를 담은 변수 p 생성
  p = ''
  for i in s:
    p += i*r
  
  result.append(p)
  
for i in result:
  print(i)
