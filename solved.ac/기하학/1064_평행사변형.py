# 내 풀이 52ms
import sys
input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())
if (xa-xb)*(ya-yc) == (xa-xc)*(ya-yb):       # a를 기준으로 b와 c의 기울기 확인, 같으면 -1 출력
    print(-1.0)
else:                        
    ab = ((xa-xb)**2 + (ya-yb)**2) ** 0.5    # 좌표 이용해서 선분 길이 구하기
    bc = ((xb-xc)**2 + (yb-yc)**2) ** 0.5
    ca = ((xc-xa)**2 + (yc-ya)**2) ** 0.5

    abc = sorted([ab, bc, ca])               # 가장 큰 둘레 길이 - 작은 둘레 길이 구하기
    print(2*(abc[2]-abc[0]))

'''
1. 직선 위에 세 점이 있을 경우 평행사변형을 만들 수 없음
	 -> a점을 기준으로 b, c의 기울기를 구해서 같으면 -1 출력  

2. 주어진 좌표로 선분 ab, bc, ca를 구한다
	 (두 변을 기준으로 하는 평행사변형을 총 3개 만들 수 있음)

3. 변의 길이가 x > y > z 라고 치면
	 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이는 (2(x+y) - 2(y+z)) -> 2(x-z)가 됨
'''