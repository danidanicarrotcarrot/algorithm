# 내 풀이
def solution(s):
    s = sorted(map(int, s.split()))            # 정렬해서 맨 앞 원소랑 맨 뒤 원소 출력
    return ' '.join(map(str, (s[0], s[-1])))

'''
쉬웠다
'''

# 다른 사람 풀이
def solution2(s):
    s = list(map(int,s.split()))              # min max로 최댓값 최솟값 출력
    return str(min(s)) + " " + str(max(s))