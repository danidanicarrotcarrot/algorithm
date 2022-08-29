# DFS와 BFS

from collections import deque
import sys

def start():
    input=sys.stdin.readline
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)] 
    
    for _ in range(m):
        x, y = map(int, input().split()) # 노드 연결
        graph[x].append(y)
        graph[y].append(x)

    for i in range(n+1): # 하아ㅏ..... 정렬ㄹㄹ.........
        graph[i].sort()
    
    visited1 = [False] * (n+1)
    visited2 = [False] * (n+1)
    
    dfs(graph, v, visited1)
    print()
    bfs(graph, v, visited2)
    
def dfs(graph, v, visited):
    visited[v] = True # 방문처리
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, s, visited):
    q = deque([s])
    visited[s] = True # 방문처리

    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
        
start()