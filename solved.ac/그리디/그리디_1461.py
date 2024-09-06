# 그리디_1461.py
# 도서관 / 골드 5


## 내 풀이
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
loc = list(map(int, input().split()))

pos = sorted([abs(i) for i in loc if i>=0], reverse=True)
neg = sorted([abs(i) for i in loc if i<=0], reverse=True)

ans = []

for p in pos[::M]:
	ans.append(p)

for n in neg[::M]:
	ans.append(n)

print(sum(ans)*2 - max(ans))