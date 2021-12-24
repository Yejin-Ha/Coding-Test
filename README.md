# 자주 사용되는 꿀팁 정리

* `input()` 대신 `sys.stdin.readline()`사용하기<br/>
  반복으로 여러 줄을 입력받아야 할 때는 input()을 사용하면 시간초과가 발생할 수 있다.<br/>
  이런 상황에서는 sys.stdin.readline()을 사용하면 시간초과가 발생하지 않는다.<br/>
  sys.stdin.readline()로 문자열을 입력받으면 개행문자(\n)가 기본으로 추가된다.(형변환을 하면 사라짐)<br/>
  
  ```python
  <!--  문자열을 입력받을 경우  -->
  import sys
  a = int(sys.stdin.readline())
  
  <!--  문자열을 여러번 입력받을 경우  -->
  import sys
  n = int(sys.stdin.readline())
  data = [sys.stdin.readline().strip() for i in range(n)]
  # strip() : \n을 기준으로 문자열을 분리한다
  ```
