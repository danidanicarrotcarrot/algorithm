# 내 풀이
def solution(ingredient):
    burger = []
    cnt = 0
    for i in ingredient:
        burger.append(i)
        if burger[-4:] == [1, 2, 3, 1]:
            cnt += 1
            del burger[-4:]
    return cnt

'''
다른 풀이도 비슷한 것 같아서 가져오지 않았다
'''