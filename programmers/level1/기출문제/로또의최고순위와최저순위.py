# 내 풀이
def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}        # { 당첨번호 개수 : 순위 }
    zero = lottos.count(0)                            # 0 개수 카운트
    lotto = len([1 for i in lottos if i in win_nums]) # 로또 당첨된 번호들만 담아줌
    return rank[lotto+zero], rank[lotto]              # 최대순위, 최소순위 출력

# 다른 사람 풀이
def solution2(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

'''
나름 잘 풀었다고 생각했는데..
교집합 대애박
'''