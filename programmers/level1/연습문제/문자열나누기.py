# 내 풀이
from collections import deque

def solution(s):
    q = deque(s)                    # ['b', 'a', 'n', 'a', 'n', 'a']
    d = {'x':1, 'y':0}              # x -> 첫 글자 횟수/ y -> x가 아닌 글자 횟수
    x = q.popleft()                 # 첫 글자
    cnt = 1
    
    while q:
        y = q.popleft()             # 다음 글자

        if x == y:                  # 첫글자랑 다음 글자랑 같으면 d['x'] + 1
            d['x'] += 1
        elif x != y:                # 다르면 d['y'] += 1
            d['y'] += 1

        if d['x'] == d['y'] and len(q):     # x 횟수 = y 횟수 + q가 있을 경우
            d['x'], d['y'] = 1, 0           # 딕셔너리 초기화
            x = q.popleft()                 # 새로운 x
            cnt += 1                        # cnt + 1
    
    return cnt

# 다른 사람 풀이
def solution2(s):
    answer = 0
    sav1=0
    sav2=0
    for i in s:
        if sav1==sav2:
            answer+=1
            a=i
        if i==a:        # 같은 글자면 sav1 횟수 + 1
            sav1+=1
        else:           # 다른 글자면 sav2 횟수 + 1
            sav2+=1
    return answer

'''
문자열을 q에 넣고 앞에서부터 하나씩 꺼내서 비교, 딕셔너리 이용해서 횟수 카운트
다른 사람 풀이를 보니까 너무 어렵게 푼 것 같다는 생각이 든다.. ㅎㅎ
'''