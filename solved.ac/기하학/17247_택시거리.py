# 내 풀이 140ms
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [list(input().split()) for _ in range(n)]

taxi = []

for y in range(n):
    for x in range(m):
        if d[y][x] == '1':
            taxi.append(x)
            taxi.append(y)
            break
            
print(abs(taxi[0]-taxi[2]) + abs(taxi[1]-taxi[3]))

'''
ax, ay, bx, by 좌표를 구해서 거리 출력
'''