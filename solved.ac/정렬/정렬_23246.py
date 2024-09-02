# Sport Climbing Combined

import sys
input = sys.stdin.readline

## 내 풀이
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

total = [[p*q*r, p+q+r, b] for b, p, q, r in lst] # 곱, 합, 등번호 순
total.sort() # 오름차순으로 정렬

for t in total[:3]:
	print(t[2], end=' ')


## 다른 풀이
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

infos = sorted(infos, key= lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for b, p, q, r in infos[:3]:
	print(b, end=' ')