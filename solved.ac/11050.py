# 이항 계수 1

def factorial(n):
    ans = 1
    for i in range(n, 1, -1):
        ans *= i
    return ans

n, k = map(int, input().split())
print(factorial(n)//(factorial(n-k)*factorial(k)))