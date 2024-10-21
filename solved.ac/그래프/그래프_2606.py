# 그래프_2606.py
# 바이러스 / 실버 3

import sys
input = sys.stdin.readline
from collections import deque

# dfs 풀이
def dfs(node):
	global adj_list, visitied, cnt

	# base case
	if visited[node]:
		return
	visited[node] = True
	cnt += 1

	# recursive case
	for adj_node in adj_list[node]:
		dfs(adj_node)

# bfs 풀이
def bfs(node):
	global adj_list, visited, cnt

	q = deque()
	q.append(node)
	visited[node] = True

	while q:
		node = q.popleft()
		cnt += 1

		for adj_node in adj_list[node]:
			if not visited[adj_node]:
				q.append(adj_node)
				visited[adj_node] = True

# input
N = int(input())
M = int(input())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
	x, y = map(int, input().split())
	adj_list[x].append(y)
	adj_list[y].append(x)

# solve
visited = [False] * (N+1)
cnt = 0
dfs(1); print(cnt-1)
# bfs(1); print(cnt-1)