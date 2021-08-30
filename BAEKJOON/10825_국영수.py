'''
# 국영수

- sorted() 의 key 속성을 이용하면 된다.
'''
stu_no = int(input())
students = []

for no in range(stu_no):
    [name, k, e, m] = input().split()
    # 모두 str type이라서 형변환을 해야 정렬이 가능하다.
    students.append([name, int(k), int(e), int(m)])

# key를 중심으로 값이 정렬된다.
# 양수라면 오름차순, 음수라면 내림차순으로 정렬된다.
# 중복되는 값이 존재한다면 뒤의 조건에 맞게 정렬한다.  
    # 예를 들면 -x[1]에서 중복된다면 x[2]에 맞게..
sorted_stu = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in sorted_stu:
    print(student[0])
