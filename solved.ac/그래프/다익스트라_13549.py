# 다익스트라_13549.py
# 숨바꼭질 3 / 골드 5

from queue import PriorityQueue

INF = int(1e12)
MAX = int(1e5)

# input
N, K = map(int, input().split())

# solve
time = [INF] * (MAX+1)

pq = PriorityQueue()
time[N] = 0
pq.put([0, N])

while not pq.empty():
	cur_time, cur_pos = pq.get()

	nxts = [[cur_time+1, cur_pos+1], [cur_time+1, cur_pos-1], [cur_time, cur_pos*2]]

	for nxt_time, nxt_pos in nxts:
		if (0 <= nxt_pos <= MAX):
			if nxt_time < time[nxt_pos]:	# time이 더 작을 때에만 갱신
				time[nxt_pos] = nxt_time
				pq.put([nxt_time, nxt_pos])

print(time[K])