"""
while문에서 EOF를 활용하는 문제(EOF:end of file)
try except 문을 통해서 입력이 되지 않은 상태라면 error를 발생시켜서 while문을 종료한다.
"""

result = []
while True:
  try:
    A, B = map(int, input().split(' '))
    result.append(A+B)
  except:
    for i in result:
      print(i)
    break
