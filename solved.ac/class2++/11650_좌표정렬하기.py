import sys
input = sys.stdin.readline

res = [list(map(int, input().split())) for i in range(int(input()))]
res.sort(key = lambda x: (x[0], x[1]))
for i in res:
    print(*i)