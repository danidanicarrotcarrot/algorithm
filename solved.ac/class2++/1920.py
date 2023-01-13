# 수 찾기

n = int(input())
nlist = set(input().split())

m = int(input())
mlist = list(input().split())

for i in mlist:
    print(1) if i in nlist else print(0)