# 내 풀이 (36ms)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [input().strip() for i in range(N)]

cnt = 0

for x in range(N):                                    # '-' 확인
    a = '/'
    for y in range(M):
        if graph[x][y] == '-' and graph[x][y] != a:   # -이면서 a와 다른 값만 +1
            cnt += 1
        a = graph[x][y]                               # a 업뎃

for y in range(M):                                    # '|' 확인 / x, y 만 변경
    a = '/'
    for x in range(N):
        if graph[x][y] == '|' and graph[x][y] != a:
            cnt += 1
        a = graph[x][y]

print(cnt)

'''
처음엔 dfs나 bfs를 활용해보려고 했는데 잘 안돼서 그냥 가로 세로로 각각 세자! 하고 풀었음
'''