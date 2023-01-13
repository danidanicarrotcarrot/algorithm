# ㄴㅍㅇ
from itertools import combinations
def solution(nums):
    com = sorted(list(map(sum, combinations(nums, 3))))  # 3개씩 묶어서 sum, 리스트에 담고 정렬
    cnt = 0
    for i in com:                                        # 걍 소수 찾는거
        for j in range(2, int(i**0.5)+1):
            if not i%j :
                break
        else:                                            # for문에 걸리지 않으면 (소수면) cnt +1
            cnt += 1
    return cnt

'''
다른 풀이도 비슷해서 그냥 가져오지 않았다
'''