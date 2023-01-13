# ㄴㅍㅇ

def solution(N, stages):
    ratio = []
    
    for stage in range(1, N+1):
        
        if not stage in stages:                                 # 해당 스테이지 유저가 없으면 실패율 0으로 처리
            ratio.append([stage, 0])
        else:
            clear = []                                          # 클리어 리스트
            fail = 0                                            # 해당 스테이지 도전 중인 유저 카운트
            for user in stages:
                if user == stage:                               # 도전중인 유저를 만나면 fail + 1
                    fail += 1
                elif user > stage :                             # 유저가 스테이지보다 높으면 clear에 담아준다
                    clear.append(user)
            ratio.append([stage, fail/(len(clear)+fail)])       # [stage, 실패율] 로 append
            stages = clear                                      # 다음 스테이지 계산 (해당 스테이지 이하 유저는 빠지게 됨)
        
    ans = sorted(ratio, key=lambda x : x[1], reverse = True)    # 실패율 기준으로 내림차순 정렬
    
    return [i[0] for i in ans]                                  # stage만 출력


'''
진짜 너무 힘들었다
주석.. 나중에 달아야지

처음에 자꾸 70점 나와서 뭐지 하고 봤는데 해당 스테이지에 유저가 없을 때 실패율 0으로 처리
하는걸 안 해서 그랬었다
수정한 다음에는 자꾸 97점 나오고 22번 테스트케이스만 시간초과떠서 빡쳤었는데 enumerate 빼니까 됐다.
시간복잡도... 열받아.. 
'''