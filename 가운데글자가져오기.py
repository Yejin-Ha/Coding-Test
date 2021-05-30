'''
# 문제
> 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항
> s는 길이가 1 이상, 100이하인 스트링입니다.

# 입출력 예
s = 'abcde' -> return 'c'
s = 'qwer' -> return 'we'
'''
def solution(s):
    leng = len(s)
    mid = leng // 2
    
    if leng % 2:
        answer = str[mid]
    else:
        mid = leng // 2
        answer = str[mid-1:mid+1]
    
    return answer
