# 숫자 카드 2
import sys
input = sys.stdin.readline

n = input()
n_ = list(map(int, input().split()))
m = input()
m_ = list(map(int, input().split()))

ans = [0] * 20000001

for i in n_ :
    ans[i] += 1

for i in m_:
    print(ans[i], end=' ')