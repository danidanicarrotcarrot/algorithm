# 내 풀이

def solution(msg):
    idx = {chr(i):i-64 for i in range(65, 91)} # A-Z까지 인덱스로 만들어줌
    res = []                        # 출력값 리스트
    w = msg[0]                      # 현재입력 w 초기값 세팅
    i = 1
    
    while True:    
        if i == len(msg):           # i가 msg길이와 같은 경우, w를 res에 넣어주고 종료
            res.append(idx[w])
            break
            
        c = w + msg[i]              # 다음글자 c
        
        if c in idx:                # c가 idx에 있으면 w를 c로 설정
            w = c
            
        else:                       # 아니면 w를 넣어주고 c를 사전에 추가
            res.append(idx[w])
            idx[c] = len(idx)+1
            w = msg[i]              # w 업뎃
            
        i += 1                      # i에 1추가
            
    return res

'''
시키는대로 구현한 것 같다
정직한 풀이 ?!
'''