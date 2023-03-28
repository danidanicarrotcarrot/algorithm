# 내 풀이 40ms
for i in range(int(input())):
    w = list(input().split())
    stack = []
    while w:
        stack.append(w.pop())
    s = ' '.join(stack)
    print(f'Case #{i+1}: {s}')

'''
그냥 스택이라길래 이렇게 풀었다..!
'''

# 내 풀이2 40ms
for i in range(int(input())):
    w = list(input().split())[::-1]
    s = ' '.join(w)
    print(f'Case #{i+1}: {s}')

'''
슬라이싱으로 리스트 순서를 뒤집어줌
'''