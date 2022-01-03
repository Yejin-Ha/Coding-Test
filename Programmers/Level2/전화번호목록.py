# 답변 1 : 95.8
def solution1(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    
    while len(phone_book) > 1:
        if phone_book[0] == phone_book[1][:len(phone_book[0])]:
            answer = False
            break
        else:
            phone_book.pop(0)
    return answer
