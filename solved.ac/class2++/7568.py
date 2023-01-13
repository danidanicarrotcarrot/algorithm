# 덩치

p1 = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(len(p1)):
    cnt = 1
    for j in range(len(p1)):
        if p1[i][0] < p1[j][0] and p1[i][1] < p1[j][1]:
            cnt += 1
    print(cnt, end=' ')