# 내 풀이
def solution(survey, choices):
    test = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for s, c in zip(survey, choices):
        if c > 4 :              # 동의
            test[s[1]] += c-4   # 첫번째 캐릭 점수 추가
        if c < 4:               # 비동의
            test[s[0]] += 4-c   # 두번째 캐릭 점수 추가

    v = [list(test.values())[i:i+2] for i in range(0, 8, 2)]    # [[0,3],[1,0],[0,2],[1,1]]
    k = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    ans = ''
    
    for i in range(4):
        if v[i][0] >= v[i][1]:      # [0,3] 비교해서 더 큰 값의 지표를 ans에 추가해줌
            ans += k[i][0]
        else:
            ans += k[i][1]
    
    return ans

'''
문제가 길어서 힘들었다
'''