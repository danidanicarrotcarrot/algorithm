# 내 풀이
def solution(n):
    nums = [i for i in range(1, n+1)]   # 1 ~ n 까지 정수 리스트 생성
    
    cnt = 0                   
    for num in nums:           # 1부터 하나씩 꺼내서
        ans = num              # ans에 1 미리 대입
        
        while ans+num <= n:    # 15보다 같거나 작을때만
            num += 1           # num 에는 1 씩 추가 ex 2, 3, 4, 5...
            ans += num         # ans 에는 num 추가 ex 1 + 2 + 3 + 4 + 5 
            
        if ans == n:           # 15랑 같으면 횟수 카운트
            cnt += 1
        
    return cnt

'''
음.. for + while이라 헷갈려서 생각보다는 오래걸렸다..!
'''