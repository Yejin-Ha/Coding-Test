'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# 입출력 예제
no	new_id      	result
예1	"...!@BaT#*..y.abcdefghijklm"       	"bat.y.abcdefghi"
예2	"z-+.^."	        "z--"
예3	"=.="       	"aaa"
예4	"123_.def"	        "123_.def"
예5	"abcdefghijklmn.p"	        "abcdefghijklmn"

'''
new_id ="abcdefghijklmn.p"

def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    result = []
    for x in new_id:
        if not x.isalpha() and not x.isdigit():
            if x in ['-', '_', '.']:
                result.append(x)
        else:
            result.append(x)

    # 3단계
    i = 0
    while i<len(result)-1:
        text = result[i]+result[i+1]
        if text == '..':
            result.pop(i+1)
        else:
            i += 1

    # 4단계
    if result[0] == '.':
        if len(result) == 1:
            result = []
        else:
            result.pop(0)

    if len(result) > 1 and result[-1] == '.':
        result.pop()

    # 5단계
    if len(result) == 0:
        result.append('a')

    # 6단계
    if len(result) > 15:
        result = result[:15]
        if result[-1] == '.':
            result.pop()
            
    # 7단계
    if len(result) < 3:
        while len(result) < 3:
            result.append(result[-1])
            print(result)

    return ''.join(result)