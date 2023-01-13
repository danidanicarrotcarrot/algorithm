# 내 풀이
from itertools import combinations

def solution(number):
    ans = list(combinations(number, 3))              # 3개씩 묶어서 조합
    return len([sum(i) for i in ans if not sum(i)])  # 그 중에서 sum이 0일때만 리스트에 넣고 개수로 리턴

# 다른 사람 풀이
def solution2(number) :
    from itertools import combinations
    cnt = 0
    for i in combinations(number,3) :
        if sum(i) == 0 :
            cnt += 1
    return cnt

'''
ㅎㅅㅎ
'''