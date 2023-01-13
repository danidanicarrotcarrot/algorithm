# 블랙잭

import itertools

_, m = map(int, input().split())
data = list(map(int, input().split()))

com = [sum(i) for i in itertools.combinations(data, 3)]

ans = [j for j in com if j <= m]

print(max(ans))