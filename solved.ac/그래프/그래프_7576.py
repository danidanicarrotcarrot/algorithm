# 그래프_7576.py
# 토마토 / 골드 5 / bfs 풀이

import sys
input = sys.stdin.readline
from collections import deque

INF = int(1e12)

# input
M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

# solve
q = deque()
time = [[INF]*M for _ in range(N)]

for y in range(N):
	for x in range(M):
		if tomato[y][x] == 1:
			q.append((y, x))
			time[y][x] = 0

while q:
	y, x = q.popleft()

	nxts = [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]
	for ny, nx in nxts:
		if not (0<=ny<N and 0<=nx<M):		# 좌표를 벗어나거나
			continue
		if time[ny][nx] <= time[y][x]+1:	# 이전 날짜보다 작거나
			continue
		if tomato[ny][nx] == -1:			# 토마토가 없으면 > 건너뜀
			continue

		q.append((ny, nx))
		time[ny][nx] = time[y][x]+1

ans = -1
for y in range(N):
	for x in range(M):
		if tomato[y][x] != -1:
			ans = max(ans, time[y][x])

print(ans if ans != INF else -1)