import sys
input = sys.stdin.readline

ans = [list(input().split()) for i in range(int(input()))]
ans.sort(key = lambda x:int(x[0]))
for a in ans:
    print(int(a[0]), a[1])