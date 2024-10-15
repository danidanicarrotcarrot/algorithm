# 이분탐색_3020.py
# 개똥벌레 / 골드 5

import sys
input = sys.stdin.readline

# input
N, H = map(int, input().split())

tops = [0] * (H+1)
bots = [0] * (H+1)

for i in range(N):
	num = int(input())
	if i%2 == 0:
		bots[num]+=1
	else:
		tops[H-num+1]+=1

# print(bots, tops) # [0, 1, 1, 4, 1, 0] [0, 0, 2, 3, 2, 0]

# solve
mn = int(1e12) 	# 파괴할 장애물의 최솟값
mn_num = 0		# 구간의 수

cnt = N//2
for h in range(1, H+1):
	cnt -= bots[h-1]
	cnt += tops[h]

	if mn == cnt:
		mn_num += 1

	if mn > cnt:
		mn = cnt
		mn_num = 1

print(mn, mn_num)
