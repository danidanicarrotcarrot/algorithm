# 내 풀이 (36ms)

from itertools import combinations
n = sorted([int(input()) for i in range(9)])  # 9개 받고

for cm in list(combinations(n, 7)):           # 7개씩 조합
    if sum(cm) == 100:                        # 조합의 합이 100이면 출력
        for i in cm:
            print(i)
        break

'''
풀이 찾아봤는데 대부분 비슷하당
'''