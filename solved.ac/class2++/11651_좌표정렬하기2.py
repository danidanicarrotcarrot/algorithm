import sys
input = sys.stdin.readline

ans = [list(map(int, input().split())) for i in range(int(input()))]
ans.sort(key = lambda x: (x[1], x[0]))
for i in ans:
    print(*i)