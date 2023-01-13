# 다현 풀이
def solution(d, budget):
    d.sort()
    cnt = 0
    while d:
        budget -= d.pop(0)  # d에서 하나씩 꺼내서 예산에서 빼줌
        if budget < 0:      # 예산이 0보다 작아지면 스탑
            break
        else:               # 아니면 cnt += 1
            cnt += 1
    return cnt

# 다른 사람 풀이
def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

'''
와우 sum을 해서 비교... 길이로 카운트 ... ㅎㅎ......... 멋잇당
'''