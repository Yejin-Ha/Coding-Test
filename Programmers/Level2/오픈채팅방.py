def solution(record):
    user = {}
    ment = []
    seq = []
    
    for r in record:
        s = r.split(' ')
        
        if s[0] == 'Enter':
            user[s[1]] = s[2]
            ment.append('님이 들어왔습니다.')
            seq.append(s[1])
        elif s[0] == 'Leave':
            ment.append('님이 나갔습니다.')
            seq.append(s[1])
        else:
            user[s[1]] = s[2]
    
    answer = [user[seq[i]] + ment[i] for i in range(len(seq))]
    
    return answer
