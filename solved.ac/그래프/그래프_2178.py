# 그래프_2178.py
# 미로 탐색 / 실버 1

# bfs
import sys
input = sys.stdin.readline
from collections import deque

# 방향
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# input
N, M = map(int, input().split())
matrix = ['0' * (M+1)] + ['0'+input() for _ in range(N)] # 그래프 구성

# solve
q = deque()
visited = [[False]*(M+1) for _ in range(N+1)]

q.append((1, 1, 1)) # (dist, y, x)
visited[1][1] = True

while q:
	dist, y, x = q.popleft()

	if y == N and x == M: # 종료조건
		print(dist)
		exit()

	for i in range(4):
		ny = y+dy[i]
		nx = x+dx[i]
		# 행렬 안 벗어남, 방문처리 false, 수가 1인것만 확인
		if (1<=ny<=N and 1<=nx<=M) and (not visited[ny][nx]) and (matrix[ny][nx] == '1'):
			q.append((dist+1, ny, nx))
			visited[ny][nx] = True


print(-1)