# 내 풀이

def solution(elements):
    s = set(elements)                        # 길이가 1인 연속 부분 수열 추가
    s.add(sum(elements))                     # 길이가 5인 연속 부분 수열 추가
    
    for i in range(1, len(elements)-1):
        ans = elements + elements[:i] + [0]  # 인덱스 맞추려고 0 추가
        for j in range(0, len(ans)-1):
            s.add(sum(ans[j:j+i+1]))         # 슬라이싱으로 2, 3, 4 연속 부분 수열에서 나올 수 있는 합 s에 추가
        
    return len(s)

'''
필요한만큼 elements를 이어 붙인다음 슬라이싱으로 답을 구함
'''