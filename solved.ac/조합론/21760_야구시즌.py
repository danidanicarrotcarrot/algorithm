# 내 풀이 48ms

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k, d = map(int, input().split())
    b = 2*d//(m*n*(k*(m-1)+m*(n-1)))
    if b:
        print(k*b*n*m*(m-1)//2 + b*n*(n-1)*m*m//2)
    else:
        print(-1)

'''
공식을 잘 모르겠어서 삽질을 좀 하다가 자꾸 시간초과 나서 결국 답지 open
a와 b의 관계와 k를 이용해서 b를 한번에 구할 수 있음

전체 경기수 <= D / a = k*b 두 식을 이용해서 b에 대한 식 도출
적용해주고, b가 0 이하면 -1 출력
'''