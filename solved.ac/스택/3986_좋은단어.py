# 내 풀이 148ms

import sys
input = sys.stdin.readline

cnt = 0
for i in range(int(input())):
    
    words = input().strip()                # 문자열로 받음 'AABB'     
    stack = []
    
    for w in words:                        # 하나씩 꺼내서 stack 마지막 문자와 비교
        if len(stack) and stack[-1] == w:
            stack.pop()                    # 같으면 pop
        else:
            stack.append(w)                # 다르면 append
    
    if not len(stack):                     # stack이 비었으면 좋은단어이므로 카운트
        cnt += 1

print(cnt)

'''
괄호 문제랑 동일했당
'''