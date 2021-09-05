#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, tri):
        check_list = []
        for x in tri:
            lst = []
            for y in x:
                if y.isdigit():
                    lst.append(True)
                else:
                    lst.append(False)
            check_list.append(lst)
        
        tri_list = list()
        for x in tri:
            lst = []
            for y in x:
                lst.append(y)
            tri_list.append(lst)
        
        while True:
            for idx, x in enumerate(tri_list[:-1]):
                for n in range(0, len(x)-1):
                    a = x[n]
                    b = x[n+1]
                    c = tri_list[idx+1][n]
                    if a.isdigit() and b.isdigit():
                        if int(a) + int(b) >= 10:
                            tri_list[idx+1][n] =  str((int(a) + int(b)) % 10)
                        else:
                            tri_list[idx+1][n] =  str(int(a) + int(b))
                        check_list[idx+1][n] = True
                    elif b.isdigit() and c.isdigit():
                        if b == c:
                            x[n] = str(0)
                        elif b > c:
                            x[n] =  str(10 + (int(c) - int(b)))
                        else:
                            x[n] = str(int(c) - int(b))
                        check_list[idx][n] = True
                    elif a.isdigit() and c.isdigit():
                        if a == c:
                            x[n+1] =  str(0)
                        elif a > c:
                            x[n+1] = str(10 + (int(c) - int(a)))
                        else:
                            x[n+1] =  str(int(c) - int(a))
                        check_list[idx][n+1] = True
            result = [all(check) for check in check_list]
            if all(result):
                break
            
        return [''.join(x) for x in tri_list]

if __name__ == '__main__':
    a = Solution()
    print(a.solution(["55","?"]))