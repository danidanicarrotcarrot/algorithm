# 내 풀이 44ms
from itertools import combinations

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
    
for _ in range(int(input())):
    nums = list(map(int, input().split()))
    num = list(combinations(nums[1:], 2))
    cnt = 0
    for x, y in num:
        cnt += gcd(x, y)
    print(cnt)

'''
최대공약수 구하기만 하면 된당!
'''