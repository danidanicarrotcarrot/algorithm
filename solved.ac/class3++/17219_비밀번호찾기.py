# 내 풀이 51704	216ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 저장된 사이트 수, 찾을 사이트 수

n = {}
for _ in range(N):
    s, p = input().split()
    n[s] = p

m = [n[input().strip()] for _ in range(M)]
print(*m, sep='\n')

'''
보자마자 딕셔너리로 해야겠다고 생각함
출력할 때 하나하나 출력하는것 보다
리스트 컴프리헨션으로 받아서 한번에 출력하는 방법이 조금 더 빨랐당

# 240ms
for _ in range(M):
    print(n[input().strip()])

# 216ms
m = [n[input().strip()] for _ in range(M)]
print(*m, sep='\n')
'''