A, B, C = map(int, input().split(' '))

"""
A + B*N < C*N
위의 공식을 만족하는 N값이 손익분기점이다.
A < (C -B)*N
A/(C-B) < N 을 만족하는 수를 찾으면 된다.
하지만 1<N 이므로 +1을 한다.
"""

# 가변 비용이 판매 가격보다 크거나 같을 경우 이익이 발생하지 않는다.
if B >= C:
  print(-1)
else:
  print(int(A/(C-B)+1))
