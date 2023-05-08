import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = [i for i in range(1, n+1)]
ans = []
while q:
    for i in range(k-1):
        q.append(q.pop(0))
    ans.append(str(q.pop(0)))
print('<' + ', '.join(ans) + '>')