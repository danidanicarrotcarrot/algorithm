# 내 풀이
def solution(k, score):
    rank = []  # 명예의 전당
    res = []  # 최하위 발표 점수

    for s in score:
        rank.append(s)  # 명예의 전당에 점수 추가 + 정렬
        rank.sort()

        if len(rank) > k:
            rank.pop(0)  # 최하위 점수 pop

        res.append(rank[0])  # 발표 점수 추가

    return res


# 다른 사람 풀이
def solution2(k, score):

    q = []
    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer


'''
비슷하네요
'''
