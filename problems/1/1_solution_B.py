answer = 0
MAX = 1000

i = 0
while i < MAX:
    if i % 3 == 0:
        answer += i
    i += 3

i = 0
while i < MAX:
    if i % 5 == 0 and i % 3 != 0:
        answer += i
    i += 5

print(answer)