# 내 풀이 40ms

n = int(input())

for i in range(n-1, n-4, -1):
    n *= i

print(int(n/24))

'''
볼록 n각형의 대각선의 수 : nC2 - n
볼록 n각형의 대각선의 교점의 수 : nC4 

4개의 꼭짓점을 잡아 사각형을 만들 때마다 대각선의 교점이 하나씩 생김
'''