# 로프
# import sys
# input = sys.stdin.readline

# n = sorted([int(input()) for i in range(int(input()))])

# ans = 0
# for idx, num in enumerate(n):
#     new = (len(n) - idx) * num
#     if ans < new :
#         ans = new

# print(ans)

import sys
input = sys.stdin.readline

n = sorted([int(input()) for i in range(int(input()))])
ans = [(len(n)-idx)*num for idx, num in enumerate(n)]
print(max(ans))