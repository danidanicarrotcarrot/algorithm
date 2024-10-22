# 다익스트라_1504.py
# 특정한 최단 경로 / 골드 4

import sys
input = sys.stdin.readline
from queue import PriorityQueue

INF = int(1e12)

def dijkstra(start_node):
	global N, adj_list

	dist = [INF] * (N+1)

	pq = PriorityQueue()
	dist[start_node] = 0
	pq.put([0, start_node])

	while not pq.empty():
		cur_dist, cur_node = pq.get()
		for adj_node, adj_dist in adj_list[cur_node]:
			temp_dist = cur_dist+adj_dist
			if temp_dist < dist[adj_node]:
				dist[adj_node] = temp_dist
				pq.put([temp_dist, adj_node])

	return dist

# input
N, E = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for _ in range(E):
	a, b, c = map(int, input().split())
	adj_list[a].append([b, c])
	adj_list[b].append([a, c])

v1, v2 = map(int, input().split())

# solve (dijkstra) 
dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)	# 꼭 지나야 하는 정점 v1, v2를 시작으로 하는 다익스트라를 돌려줌
dist_v2 = dijkstra(v2)

case1 = dist_1[v1] + dist_v1[v2] + dist_v2[N] # 1 - v1 - v2 - N
case2 = dist_1[v2] + dist_v2[v1] + dist_v1[N] # 1 - v2 - v1 - N

best = min(case1, case2) # 둘 중 최소값

print(best if best < INF else -1)