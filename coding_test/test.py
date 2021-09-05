code = "abcdefghijklmnopqrstuvwxyz"
message = "test"
# message = "20051920"

code_num = dict()
answer = ""

for idx, a in enumerate(code, start=1):
    if idx < 10:
        idx = '0'+str(idx)
    else:
        idx = str(idx)
    code_num.update({a:idx})

if message.isdigit():
    for n in range(0, len(message), 2):
        for key, val in code_num.items():
            if val == message[n:n+2]:
                answer += key
else:    
    for t in message:
        answer = answer + code_num[t]


print(answer)
