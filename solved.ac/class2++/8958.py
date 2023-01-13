# OX퀴즈

t = int(input())

for i in range(t):
    ox = list(input())
    count, score = 0, 0
    for j in range(len(ox)):
        if ox[j] == 'O':
            count += 1
            score += count
        if ox[j] == 'X':
            count = 0 # x면 count를 리셋시키기 ~
    print(score) 