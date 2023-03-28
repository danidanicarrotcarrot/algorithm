# 내 풀이

def primenumber(x):                     # 소수 판별용 함수
    for i in range(2, int(x**0.5)+1):
    	if x % i == 0:		
        	return False
    return True

def solution(n, k):
    x = []                              # k진수 만들기
    while n:
        x.append(n%k)                   # x에 나머지를 계속 담아주고 n은 k로 나눈 몫으로 초기화
        n //= k
    nums = ''.join(map(str, x))[::-1]   # 리스트에 담은 값을 join으로 합쳐주고 역순으로 -> k진수 완성 ~
    nums = nums.split('0')              # k진수로 변환한 값을 0을 기준으로 스플릿
    
    cnt = 0
    for num in nums:                    # 하나씩 가져와서 소수인지 판별
        if num == '1':
            continue
        elif num.isdigit() and primenumber(int(num)):
            cnt += 1
    
    return cnt

'''
내 풀이에서는 0으로 스플릿하는 게 핵심이었당
예를들어 n = 110011 이면 -> ['11', '', '11'] 로 바뀌고
해당 원소들이 소수인지 판별하면 끝..
풀 때 k진수로 바꾸고, 또 자르고, 소수인지 판별하고 그래야돼서 굉장히 복잡하게 느껴졌다

테스트 1 〉	통과 (96.34ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (0.04ms, 10.5MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.04ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.4MB)
테스트 8 〉	통과 (0.04ms, 10.4MB)
테스트 9 〉	통과 (0.05ms, 10.4MB)
테스트 10 〉	통과 (0.04ms, 10.4MB)
테스트 11 〉	통과 (0.04ms, 10.4MB)
테스트 12 〉	통과 (0.04ms, 10.4MB)
테스트 13 〉	통과 (0.04ms, 10.4MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.04ms, 10.5MB)
테스트 16 〉	통과 (0.04ms, 10.5MB)
'''