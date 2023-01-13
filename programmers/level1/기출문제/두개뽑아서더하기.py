# 내 풀이
from itertools import combinations

def solution(numbers):
    a = list(combinations(numbers, 2))
    res = [sum(i) for i in a]       # 두 개씩 뽑아서 더하기
    return sorted(list(set(res)))   # 중복 제거

# 다른 사람 풀이
def solution2(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

'''
음.. 비슷하다 다만 combinations를 쓰고 안 쓰고?
'''