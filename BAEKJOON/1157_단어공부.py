# 입력받은 문자열을 다 대문자로 치환
input_string = input().upper()

# key:문자, value:문자개수 인 dictionary 생성
result = {}

for s in input_string:
  if s not in result:
    result[s] = input_string.count(s)
