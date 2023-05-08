import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
stack = [i for i in range(1, nums[0]+1)]
ans = '+'*nums[0]

i = nums[0]+1
j = 0

while j != n:
    if len(stack) == 0:
        stack.append(i)
        ans += '+'
        i += 1
    else:
        m = stack[-1]
        if nums[j] == m:
            stack.pop()
            ans += '-'
            j += 1
        elif nums[j] > m :
            stack.append(i)
            ans += '+'
            i += 1
        else:
            print('NO')
            exit()
            
for i in ans:
    print(i)