from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in sorted(map(sum, combinations(num, 3))):
    if i > m:
        break
    ans = i
print(ans)