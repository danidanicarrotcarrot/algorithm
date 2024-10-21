# 그래프_1697.py
# 숨바꼭질 / 실버 1

# bfs
from collections import deque
import sys
input = sys.stdin.readline

MAX = int(1e5)

# input
N, K = map(int, input().split())

# solve
q = deque()
visited = [False] * (MAX+1)

q.append((0, N)) 	# time, position
visited[N] = True

while q:
	time, pos = q.popleft()
	
	if pos == K:	# 종료 조건
		print(time)
		exit()

	for nxt_pos in [pos+1, pos-1, pos*2]:
		if (0<=nxt_pos<=MAX) and (not visited[nxt_pos]):
			q.append((time+1, nxt_pos))
			visited[nxt_pos] = True