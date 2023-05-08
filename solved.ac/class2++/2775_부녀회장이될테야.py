import sys
input = sys.stdin.readline

for i in range(int(input())):
    k = int(input())
    n = int(input())
    apt = [[i for i in range(1, n+1)]]
    for i in range(k):
        apt.append([1])

    for i in range(1, k+1):
        for j in range(1, n):
            apt[i].append(apt[i-1][j]+apt[i][j-1])

    print(apt[-1][-1])