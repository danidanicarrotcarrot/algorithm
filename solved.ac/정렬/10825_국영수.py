# 내 풀이
N = int(input())
score = []

for i in range(N):
    [name, kor, eng, math] = map(str, input().split())
    score.append([name, int(kor), int(eng), int(math)])

ss = sorted(score, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in ss:
    print(s[0])