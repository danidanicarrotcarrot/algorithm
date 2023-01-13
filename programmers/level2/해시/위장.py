def solution(clothes):
    res = {}
    for cname, ctype in clothes:
        res[ctype] = res.get(ctype, 0) + 1
    
    ans = 1
    for ctype in res:
        ans *= (res[ctype]+1)
    
    return ans-1