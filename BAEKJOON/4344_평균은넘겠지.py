n = int(input())

# 결과를 저장할 1차원 배열 생성
result = []

# 입력받은 n번만큼 반복
for _ in range(0, n):
  scores = list(map(int, input().split(' ')))

  # 학생의 수를 num 변수로 분리
  num = scores.pop(0)
  
  # 전체 학생의 평균 점수 구하기
  mean_score = sum(scores)/num

  # 평균을 넘는 학생들의 수 구하기 
  counts = [0 for s in scores if s > mean_score]
  
  # result 배열에 평균을 넘는 학생의 비율을 추가
  result.append(len(counts)/num*100)
  
for i in result:
  print("{:.3f}%".format(i))

"""
소수점 표현하는 함수 : format(), round()
* {:.3f}.format(숫자)
  - 소수점 3번째 숫자까지 출력한다.
  - 자동으로 반올림을 한다.
  - 만약 숫자가 없다면(1.0, 2.22 등) 0으로 출력한다.(1.0 -> 1.000)
  
* round(숫자, 자리수)
  - 원하는 자리수까지 반올림한다.
  - 숫자가 없다면 출력하지 않는다.(round(1.10, 3) = 1.1
"""
