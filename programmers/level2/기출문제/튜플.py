# 내 풀이

def solution(s):
    s = s.replace('{', '')
    s = s.replace('}}', '')
    s = s.split('},') 
    nums = [i.split(',') for i in s] # [["1","2","3"],["2","1"],["1","2","4","3"],["2"]]
    nums.sort(key=len)               # [["2"],["2","1"],["1","2","3"],["1","2","4","3"]] 길이순으로 정렬
    
    ans = []
    for num in nums:
        for n in num:
            n = int(n)
            if n not in ans:         # ans에 해당 숫자가 없는 경우 추가
                ans.append(n)
    
    return ans

'''
문자열로 주어지는 집합을 리스트 원소들로 바꿔준 다음, 원소 길이순으로 정렬함
2중 for문으로 리스트를 돌면서 답을 구했당

오랜만에 풀어서 그런가 아무것도 기억이 안 났다 그래서 이상하게 푼듯....
replace 대신 정규식을 써보고 싶었는데.. ㅎㅎ 다음에 써야지
'''