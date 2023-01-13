# 다현 풀이
def solution(arr):
    q = []
    for i in arr:
        if len(q) != 0 and q[-1] == i:  # q 길이가 0이 아니고 q 마지막 원소가 i 면 추가안함
            continue
        else:
            q.append(i)                 # 그 외엔 추가
    return q

# 다른 사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue   # [-1]로 비교하면 empty array일 때 인덱싱오류,[-1:]를 통해 리스트를 만들어 비교
        a.append(i)
    return a

'''
슬라이싱 진짜 대박 ,,
'''