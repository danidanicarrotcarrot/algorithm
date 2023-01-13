# 내 풀이(60ms)

n = int(input())
ans, cnt = 0, 0

for i in range(1, n+1): 
    ans += i       # ans에 계속 자연수를 더해주고  
    if ans > n:    # ans > n 이 되면 스탑
        break
    cnt += 1       # 개수 카운트
print(cnt)

'''
그냥 딱 1부터 쭉 더해주면 되는 문제 !
'''