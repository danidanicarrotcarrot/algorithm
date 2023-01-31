# 내 풀이 (60ms) 

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(x, y):
    q = deque()
    q.append([x,y])                                   

    while q:
        x, y = q.popleft()
        if board[x][y] == -1:                          # -1이면 끝이니까 종료
            return 'HaruHaru'    
        if not board[x][y]:                            # 칸의 값이 0인 경우 패스
            continue
        if 0 <= x + board[x][y] < N and 0 <= y < N:    # (x + 이동 가능한 칸)이 N구역 내에 있으면 q에 append
            q.append([x+board[x][y], y])
        if 0 <= x < N and 0 <= y + board[x][y] < N:    # (y + 이동 가능한 칸)이 N구역 내에 있으면 q에 append
            q.append([x, y+board[x][y]])
    
    return 'Hing'

print(bfs(0,0))

'''
그래프랑 좀 친해져야겠당
'''