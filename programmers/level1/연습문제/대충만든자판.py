# 내 풀이

def solution(keymap, targets):
    
    res = []                           # 최종 결과
    for target in targets:             # ["ABCD","AABB"]
        
        ans = []                       # 키 누르는 횟수
        for t in target:               # A가 keymap 몇번째 인덱스에 해당하는지 확인
						num = [(key.find(t)+1) for key in keymap if key.find(t) >= 0]
            if len(num):               # 인덱스가 있는 경우에만 num에 저장
                ans.append(min(num))   # num이 있으면 그 중 작은 수를 ans에 추가
            else:
                ans.append(-1)         # 인덱스가 없으면 문자열을 작성할 수 없으므로 -1 추가
                break
                
        if -1 in ans:             # -1이 ans에 있으면 res에 -1 추가
            res.append(-1)
        else:                     # 없으면 ans 다 더해서 res에 추가
            res.append(sum(ans))
    
    return res


'''
처음엔 cnt로 min(num)을 바로바로 더해주는 식으로 했는데 실패가 떴다
다른 문자열들은 다 있지만 하나라도 없으면 최종적으로 -1이 반환되어야 한다는 것을 간과했음
-> ans 리스트에 -1이 하나라도 있으면 최종적으로 -1을 리턴하는 식으로 변경해서 성공
'''