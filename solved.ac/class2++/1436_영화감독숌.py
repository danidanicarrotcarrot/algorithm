import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
six = 1
while n != cnt:
    six += 1
    if str(six).count('666') :
        cnt += 1
print(six)