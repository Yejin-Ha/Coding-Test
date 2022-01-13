def solution(s):
    table = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 
             'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    txt = ''
    answer = ''

    while s:
        if len(s) > 1:
            f_s = s[0]
            s = s[1:]
        else:
            f_s = s
            s = ''
            
        # 첫번째 글자가 숫자일 경우
        if f_s.isdigit():
            # answer에 추가한 후 계속 진행
            answer += f_s

        # 첫번째 글자가 문자일 경우
        else:
            txt += f_s
            if txt in table:
                answer += str(table[txt])
                txt = ''
                
    return int(answer)
