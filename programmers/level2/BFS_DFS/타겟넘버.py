# 내 풀이

def solution(numbers, target):
    nums = [0]
    for num in numbers:
        tmp = []
        for n in nums:
            tmp.append(n+num)
            tmp.append(n-num)
        nums = tmp
    
    cnt = 0
    for n in nums:
        if n == target:
            cnt += 1
    
    return cnt

'''
모든 계산 결과를 다 nums에 담아서 target과 비교 후 같으면 카운트 해준다
'''