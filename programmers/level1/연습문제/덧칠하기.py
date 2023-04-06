# 내 풀이

def solution(n, m, section):
    
    painted = 0                 # 이미 칠해진 부분
    cnt = 0                     # 페인트 칠한 횟수
    
    for s in section:           # 칠해야 할 구역 s
        
        if s >= painted:        # s가 painted를 넘어가는 영역이면 칠해야 하므로
            cnt += 1            # 횟수 카운트
            painted = s+m       # painted는 s+m으로 업뎃

    return cnt

'''
처음에 칠해야 하는 부분만 0으로 해서 리스트 만들고 진행했는데 시간초과 남
다시 생각해보니 이렇게 하면 될 것 같아서 바꿨당

section = [2, 3, 6] / m = 4 면
s = 2, painted = 0 -> cnt + 1, painted = 6
s = 3, painted = 6 -> pass
s = 6, painted = 6 -> cnt + 1, painted = 10 -> 종료
'''