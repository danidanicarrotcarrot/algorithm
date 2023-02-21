# 내 풀이 (44ms)
import sys
input = sys.stdin.readline

W, H, X, Y, P =  map(int, input().split())
cnt = 0

for _ in range(P):
    x, y = map(int, input().split())
    
    if X <= x <= X+W and Y <= y <= Y+H:             # 직사각형 내부에 있는 경우
        cnt += 1
        continue

    d1 = ((X-x)**2 + ((Y+H//2)-y)**2)**0.5          # 오른쪽 반원
    d2 = ((x-(X+W))**2 + (y-(Y+H//2))**2)**0.5      # 왼쪽 반원
    
    if d1 <= H//2 or d2 <= H//2:                    # 거리가 반지름과 같은 경우
        cnt += 1

print(cnt)

'''
3가지 경우로 나누어서 계산
'''