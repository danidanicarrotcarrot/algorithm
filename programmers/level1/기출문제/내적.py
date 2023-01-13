# 내 풀이
def solution(a, b):
    ans = 0
    for x, y in zip(a, b):
        ans += x*y        
    return ans

# 다른 사람 풀이
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)]) 

'''
sum을 하면 되넹
'''