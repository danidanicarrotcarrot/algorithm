import sys
input = sys.stdin.readline

while True:
    n = input().strip()
    if n == '0':
        break        
    elif n[::-1] == n:
        print('yes')
    else :
        print('no')