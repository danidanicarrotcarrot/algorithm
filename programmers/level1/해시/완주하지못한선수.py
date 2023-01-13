# 내 풀이
def solution(participant, completion):
    p = {}  # {참가자 이름:수}

    for i in participant:  # 참가자가 여러명이면 +1
        if i in p: p[i] += 1
        else: p[i] = 1

    for i in completion:  # 완주했으면 -1
        if i in p: p[i] -= 1

    return [k for k, v in p.items() if v == 1][0]  # 완주 못한 애들만 리턴


# 다른 사람 풀이
import collections


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


'''
카운터 객체는 이렇게 객체끼리 빼는게 가능하다 함 ㄷ ...........
알아두면 좋을 것 같당 ,...!
'''
