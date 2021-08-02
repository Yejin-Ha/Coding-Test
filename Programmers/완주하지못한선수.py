# 첫번째 답안 : 50점
def solution1(participant, completion):
    while len(completion):
        player = completion.pop()

        if player in participant:
            participant.pop(participant.index(player))
        
    return ''.join(participant)


# 두번째 답안 : 100점
# collection의 counter을 사용
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
