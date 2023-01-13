# 내 풀이
def solution(dartResult):
    score = []
    
    for dart in dartResult:
        
        if dart == '0' and not len(score) :    # 정수 0 처리 -> 0이 들어오고 score가 비어있으면 0 담아줌
            score.append(0)
        elif dart == '0' and score[-1] == 1:   # 정수 10 처리 -> 0이 들어왔는데 score 마지막 수가 1이면 10으로 변경
            score[-1] = 10
        elif dart.isdigit():                   # 1~9에 해당하면 그대로 score에 담아줌
            score.append(int(dart))
        
        elif dart == 'S':                      # 1제곱이니까 걍 패스
            continue
        elif dart == 'D':                      # score 마지막 수에 2제곱
            score[-1] **= 2
        elif dart == 'T':                      # score 마지막 수에 3제곱
            score[-1] **= 3
            
        elif dart == '*' and len(score) != 1:  # 스타상이 2번째나 3번째에 나왔을 경우 끝에서부터 두 수 * 2
            score[-1] *= 2  
            score[-2] *= 2
        elif dart == '*' and len(score) == 1:  # 스타상이 첫번째로 나왔으면 하나만 * 2
            score[-1] *= 2   
        elif dart == '#':                      # 아차상은 * -1
            score[-1] *= -1
    
    return sum(score)                          # 합계 출력


# 다른 사람 풀이
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

'''
정직한 풀이 ㅇㅇ...
처음이 10이랑 0 처리 안해줘서 틀렸길래 처리해주고 통과
진짜 시키는대로 구현만 함...

다른 사람 풀이를 봤는데 그저 놀랍다 .. 정규표현식...?
'''