'''
s               	        result
"aabbaccc"	                7
"ababcdcdababcdcd"	        9
"abcabcdede"	            8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	        17
'''

def solution(s):
    length = []
    result = ""

    if len(s)==1:
        print('stop')

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