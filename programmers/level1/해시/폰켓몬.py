# 내 풀이
def solution(nums):
    if len(set(nums)) > len(nums)//2:      # 주어진 폰켓몬 수랑 N/2마리 개수랑 비교
        return len(nums)//2                # ex 폰켓몬 5, N/2 3 이면 3 출력
    else:
        return len(set(nums))              # ex 폰켓몬 2, N/2 3 이면 2 출력


# 다른 사람 풀이
def solution2(ls):
    return min(len(ls)/2, len(set(ls)))    # min 써서 대소비교


'''
하고 나서 알았는데 어차피 짝수로 주어지니까 // 할 필요 없었넹
'''