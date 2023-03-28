# 내 풀이

def solution(priorities, location):
    paper = [i for i in range(len(priorities))] # [0, 1, 3, 4] 문서 번호
                                                # [2, 1, 3, 2] 문서별 중요도
    res = []
    while paper:
        p = priorities.pop(0)             # 현재 리스트에서 첫번째 문서의 중요도 p ex 2
        i = paper.pop(0)                  # 현재 리스트에서 첫번째 문서 번호 i ex 0
        
        if paper and p < max(priorities): # 리스트가 비어있지 않고, 중요도 리스트의 max값보다 해당 문서의 중요도가 낮으면
            priorities.append(p)          # 리스트 뒤에 p, i 각각 추가
            paper.append(i)
        else:
            res.append(i)                 # 그렇지 않으면 res에 문서 번호 추가

    return res.index(location)+1          # location의 인덱스 +1 로 답 구함

'''
그냥 무식하게.. 리스트를 두 개 만든 다음 큐를 활용해서 풀었음
며칠 안 했더니 실력이 제자리 걸음인 것 같아 속상하다 ㅎ
'''