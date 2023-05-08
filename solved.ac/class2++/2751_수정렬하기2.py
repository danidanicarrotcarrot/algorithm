import sys
input = sys.stdin.readline

ans = [int(input()) for _ in range(int(input()))]
ans.sort()
print(*ans, sep='\n')