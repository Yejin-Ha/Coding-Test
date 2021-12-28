def solution(s):
    length = []
    result = ""

    # 입력된 문자열의 길이가 1이라면 압출할 필요가 없기에 1을 반환한다.
    if len(s)==1:
        return 1

    for cut in range(1, len(s)//2+1):
        count = 1
        tempstr = s[:cut]

        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tempstr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result = result + str(count) + tempstr
                tempstr = s[i:i+cut]
                count = 1

        if count == 1:
            count = ""
        result += str(count) + tempstr
        length.append(len(result))
        result = ""
        
    return min(length)
