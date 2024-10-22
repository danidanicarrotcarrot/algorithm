# 다익스트라_1753.py
# 최단경로 / 골드 4

import sys
input = sys.stdin.readline
from queue import PriorityQueue

INF = int(1e12)

# input
V, E = map(int, input().split())	# 정점 V, 간선 E
K = int(input())					# 시작 정점의 번호

adj_list = [[] for _ in range(V+1)]
for _ in range(E):
	u, v, w = map(int, input().split())
	adj_list[u].append([v, w])		# 그래프에 연결노드랑 가중치 담아줌

# solve (dijkstra)
dist = [INF]*(V+1) 			# 거리 큰 값으로 담아줌

pq = PriorityQueue()
dist[K] = 0
pq.put([0, K])				# 거리, 노드 순으로 put

while not pq.empty():
	cur_dist, cur_node = pq.get()					# 현재 거리, 노드
	for adj_node, adj_dist in adj_list[cur_node]:	# 현재 노드와 연결된 노드 탐색
		temp_dist = cur_dist+adj_dist		# 현재 거리 + 가중치
		if temp_dist < dist[adj_node]:		# 더 적으면 갱신해주고 pq에 추가
			dist[adj_node] = temp_dist
			pq.put([temp_dist, adj_node])

for d in dist[1:]:
	print (d if d != INF else 'INF')