# 내 풀이
def solution(A,B):
    A, B = sorted(A), sorted(B, reverse=True)
    return sum([a*b for a, b in zip(A, B)])

'''
각각 오름차순 내림차순으로 정렬해서 하나씩 곱해줌
'''