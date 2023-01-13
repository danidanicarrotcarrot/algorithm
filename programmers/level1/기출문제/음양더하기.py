# 다현 풀이
def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):     # for 문 돌면서
        if signs[i]:                    # true면 +
            ans += absolutes[i]         
        else :
            ans -= absolutes[i]         # false면 -
    return ans

# 다른 사람 풀이
def solution2(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

'''
와 zip으로 묶어서 바로 ㄷ ... 쩐다
'''