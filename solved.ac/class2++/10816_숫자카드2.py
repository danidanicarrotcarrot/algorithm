import sys
input = sys.stdin.readline

cards = [0] * 20000001
n = int(input())
num = list(map(int, input().split()))
m = int(input())
mum = list(map(int, input().split()))

for i in num:
    cards[i] += 1

for i in mum:
    print(cards[i], end=' ')