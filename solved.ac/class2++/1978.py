# 소수 찾기

n = int(input())
nums = list(map(int, input().split()))
ans = 0

def prime(x):
    if x == 1: # 1은 소수가 x
        return False
    for j in range(2, x):
        if x % j == 0: # 0으로 나누어 떨어지면 소수 x
            return False
    return True

for i in nums:
    if prime(i) == True:
        ans += 1
    
print(ans)