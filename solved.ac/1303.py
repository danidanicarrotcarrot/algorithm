# 전쟁 - 전투

# DFS 로 접근
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]


def wdfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x >= n or x <= -1 or y >= m or y <= -1:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 'W':
        # 병사 수 추가
        w_cnt.append(1)
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        wdfs(x - 1, y)
        wdfs(x + 1, y)
        wdfs(x, y - 1)
        wdfs(x, y + 1)
        return True
    return False


def bdfs(x, y):
    # 주어진 범위 벗어나면 종료
    if x >= n or x <= -1 or y >= m or y <= -1:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 'B':
        # 병사 수 추가
        b_cnt.append(1)
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        bdfs(x - 1, y)
        bdfs(x + 1, y)
        bdfs(x, y - 1)
        bdfs(x, y + 1)
        return True
    return False


w_cnt, w_result, b_cnt, b_result = [], [], [], []

for i in range(n):
    for j in range(m):
        if wdfs(i, j):
            w_result.append(len(w_cnt)**2)
            w_cnt = []

        elif bdfs(i, j):
            b_result.append(len(b_cnt)**2)
            b_cnt = []

print(sum(w_result), sum(b_result))
