# 다현 풀이
def solution(arr1, arr2):
    ans = []
    for x, y in zip(arr1, arr2):      # 먼저 리스트별로 묶어주고
        arr = []
        for a, b in zip(x, y):        # 그 안에 각각 원소들을 더해서 arr에 담고
            arr.append(a+b)
        ans.append(arr)               # arr를 담은 ans를 리턴
    return ans

# 다른 사람 풀이 
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

'''
내 코드랑 로직은 같은데 ..
ㅎㅎ 컴프리헨션 ㄷㄷ
'''