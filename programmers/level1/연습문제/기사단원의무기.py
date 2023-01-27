# 내 풀이
def solution(number, limit, power):
    
    nums = []
    
    for i in range(1, number+1):                    # 약수 개수 체크
        cnt = set()                                 # 중복제거
        for j in range(1, int(i**0.5)+1):           # 제곱근까지만 확인
            if not i%j : cnt.add(j); cnt.add(i//j)  # 약수인 값들 추가
        
        if len(cnt) > limit:                        # 약수 개수가 limit을 초과하면 power append
            nums.append(power)
        else:                                       # 아니면 약수 개수 추가
            nums.append(len(cnt))
            
    return sum(nums)                                # 다 더해서 출력


'''
1. 1부터 number까지 약수 개수 카운트해서 nums에 추가
2. cnt > limit인 친구들은 power 추가
3. nums 합 출력

약수는 역시 제곱근까지만 체크! + 중복제거 
복습복습
'''

# 다른 사람 풀이
def cf(n): # 약수 개수 구하는 함수
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])

'''
같은 방법인데 함수를 따로 만들고 출력문을 한줄로..
'''