# 내 풀이

def solution(record):
    name = {}                           # 닉네임 기록 dict
    res = []                            # 최종 결과
    
    for r in record:
        r = r.split()                   
        if r[0] != 'Leave':             # enter or change -> 닉네임 업데이트 
            name[r[1]] = r[2]
        if r[0] != 'Change':            # enter or leave -> 결과에 [입퇴장여부, 아이디] 추가
            res.append([r[0], r[1]])
            
    for i in range(len(res)):
        if res[i][0] == 'Enter':        # 입장이면 들어왔습니다 / 아니면 나갔습니다로 닉네임 변경해서 담아주고 출력
            res[i] = f'{name[res[i][1]]}님이 들어왔습니다.'
        else:
            res[i] = f'{name[res[i][1]]}님이 나갔습니다.'
            
    return res

'''
유저 아이디로 입장/퇴장 기록해주고, 딕셔너리에 기록된 해당 아이디의 최종 닉네임으로 출력
'''