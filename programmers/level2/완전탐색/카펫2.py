# 내 풀이
def solution(brown, yellow):
    by = brown+yellow
    res = [[by//i, i] for i in range(1, int(by**0.5)+1) if not by%i] # [[12,1],[6,2],[4,3]]
    
    for r in res[::-1]:
        if (r[0]-2)*(r[1]-2) == yellow:     # x-2 * y-2 가 노란색 격자랑 같으면 출력
            return r

# 내 풀이 2 **예전에 풀었던 거
def solution2(brown, yellow):
    x = brown + yellow

    for i in range(3, int(x**0.5)+1):
        if not x%i and (i-2) * ((x//i)-2) == yellow:
            return [x//i, i]

'''
약수를 구해서 조건에 맞는지 검증했던 건 비슷한데 저번에 푼 게 더 깔끔한 것 같당
'''