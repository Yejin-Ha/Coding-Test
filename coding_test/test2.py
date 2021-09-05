#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def solution(self, instructions):
        instructions = [i.split(' ') for i in instructions]
        self.angle = 0

        for instruct in instructions:
            if len(instruct) > 1 and instruct[1].isdigit():
                if instruct[0] == 'LEFT':
                    self.LEFT(int(instruct[1]))
                elif instruct[0] == 'RIGHT':
                    self.RIGHT(int(instruct[1]))
                elif instruct[0] == 'TURN':
                    self.TRUN()
            elif instruct[0] == 'HALT':
                break
            else:
                if instruct[0] == 'LEFT':
                    self.LEFT()
                elif instruct[0] == 'RIGHT':
                    self.RIGHT()
                elif instruct[0] == 'TURN':
                    self.TRUN()

        return self.angle

    def LEFT(self, dx=90):
        self.angle -= dx
        while (self.angle >= 360 or self.angle < 0):
            if self.angle >= 360:
                self.angle -= 360
            elif self.angle < 0:
                self.angle += 360

    def RIGHT(self, dx=90):
        self.angle += dx
        while (self.angle >= 360 or self.angle < 0):
            if self.angle >= 360:
                self.angle -= 360
            elif self.angle < 0:
                self.angle += 360
    
    def TRUN(self):
        self.angle += 180
        while (self.angle >= 360 or self.angle < 0):
            if self.angle >= 360:
                self.angle -= 360
            elif self.angle < 0:
                self.angle += 360

if __name__ == '__main__':
    a = Solution()
    print(a.solution(["LEFT","LEFT","TURN AROUND"]))