# 그래프_1260.py
# DFS와 BFS / 실버 2

from collections import deque	# bfs
import sys
input = sys.stdin.readline

# dfs 깊이 우선 탐색
def dfs(node):
	global adj_list, visited_dfs	# 그래프, 방문처리 리스트

	# base case
	if visited_dfs[node]:			# 방문했다면 리턴
		return
	visited_dfs[node] = True		# 아니면 방문처리 후 출력
	print(node, end=' ')

	# recursive case				# 해당 노드와 연결된 노드 추가 후 dfs진행
	for adj_node in adj_list[node]:
		dfs(adj_node)

# bfs 너비 우선 탐색
def bfs(node):
	global adj_list, visited_bfs	# 그래프, 방문처리 리스트
	
	q = deque()						# q 생성 후 최초 노드 추가 + 방문처리
	q.append(node)					
	visited_bfs[node] = True

	while q:									# 바로 꺼내고 출력
		node = q.popleft()
		print(node, end=' ')

		for adj_node in adj_list[node]:			# 해당 노드와 연결된 노드 순차적으로 q에 추가, 방문처리
			if not visited_bfs[adj_node]:
				q.append(adj_node)
				visited_bfs[adj_node] = True


# input
N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
	x, y = map(int, input().split()) 	# 양방향 그래프로 생성
	adj_list[x].append(y)
	adj_list[y].append(x)

for node in range(1, N+1):				# 노드 정렬 
	adj_list[node].sort()

# solve
visited_dfs = [False] * (N+1)	# 방문처리용 리스트 각각 생성
visited_bfs = [False] * (N+1)

dfs(V)
print()
bfs(V)