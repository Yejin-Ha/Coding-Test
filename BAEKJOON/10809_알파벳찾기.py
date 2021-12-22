# 알파벳 리스트를 import 
from string import ascii_lowercase

s = input()

# 결과를 담을 1차원 배열
result = []

for i in ascii_lowercase:
  result.append(s.find(i))

for i in result:
  print(i, end=' ')

"""
문자열에서 원하는 문자가 있는지 찾는 함수 : find(), index()
* s.find('a') 
  - 'a'가 s에 없다면 -1을 반환한다.

* s.index('a')
  - 'a'가 s에 없다면 error를 반환한다.
"""
