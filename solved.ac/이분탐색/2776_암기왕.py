# 내 풀이 1612ms
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    memo1 = set(map(int, input().split()))
    m = int(input())
    memo2 = list(map(int, input().split()))

    for m in memo2:
        if m in memo1:
            print(1)
        else:
            print(0)


# 내 풀이2 -> 5476ms
import sys
input = sys.stdin.readline

def binary_search(left, right, memo, num):
    while left <= right:
        mid = (left+right)//2  
        if memo[mid] == num :
            return 1
        elif memo[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return 0
    
for _ in range(int(input())):
    n = int(input())
    memo1 = sorted(list(map(int, input().split())))
    m = int(input())
    memo2 = list(map(int, input().split()))
    
    for num in memo2:
        print(binary_search(0, n-1, memo1, num))

'''
set으로 풀면 되는 문제
'''