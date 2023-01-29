# 내 풀이 (208ms)

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)                       # 1번 국가 추가
    visited[x] = 1                    # 1번 국가 방문처리
    ans = 0
    
    while q:
        x = q.popleft()
        for y in graph[x]:            # 연결된 국가 확인
            if not visited[y]:        # 방문하지 않았으면 q에 추가, 방문처리
                q.append(y)       
                visited[y] = 1
                ans += 1              # 카운트 + 1
            else:
                continue
    return ans

for _ in range(int(input())):
    N, M = map(int, input().split())  # 국가, 비행기
    
    graph = [[] for i in range(N+1)]
    visited = [0 for i in range(N+1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)            # 그래프 연결
        graph[b].append(a)

    print(bfs(1))

'''
올해 그래프 첫 풀이 ㅎㅅㅎ
처음엔 좀 어려웠는데 다 풀고나니 생각보다 할만한거 같아서 다음 문제는 더 잘 풀 수 있을지도..
'''