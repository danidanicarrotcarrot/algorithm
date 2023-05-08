import sys
input = sys.stdin.readline

n = int(input())
people = [list(map(int, input().split())) for i in range(n)]
ans = []
for i in range(n):
    x = people.pop(0)
    cnt = 1
    for y in people:
        if x[0]<y[0] and x[1]<y[1]:
            cnt += 1
    ans.append(cnt)
    people.append(x)

print(*ans, sep=' ')