# 내 풀이 1104ms Python 3 / 708ms PyPy3

import sys
input = sys.stdin.readline

n = int(input())                            # 치킨집 수 8
chicken = list(map(int, input().split()))   # 치킨집 리스트
k = int(input())                            # 정렬 개수 2

chicken = [sorted(chicken[j:j+n//k]) for j in range(0, n, n//k)] # 2명이 하는거면 8//2 4만큼 움직이게 설정해서 슬라이싱한 다음 정렬
print(*[j for i in chicken for j in i])     # 이중리스트에서 꺼내고 *로 언패킹해서 출력

'''
처음엔 너무 어렵게 생각했는데
k명이 나누는거면 n//k로 범위 설정해서 슬라이싱으로 자르고 정렬해야겠다고 생각함
k = 4 -> n//k = 2 -> 2개씩 잘라서 정렬 [[1, 5], [2, 4], [2, 9], [3, 7]]
k = 2 -> n//k = 4 -> 4개씩 잘라서 정렬 [[1, 2, 4, 5], [2, 3, 7, 9]]
k = 1 -> n//k = 8 -> 8개씩 잘라서 정렬 [[1, 2, 2, 3, 4, 5, 7, 9]]
'''

# 다른 사람 풀이 656ms	PyPy3

import sys
input=sys.stdin.readline

N=int(input())
num_list=list(map(int,input().split()))

K=int(input()) #현재 정렬을 진행중인 회원의 수

new_list=[0 for _ in range(N)]

for i in range(K):
    templist=num_list[i*N//K:i*N//K+N//K]
    tempList=templist.copy()
    tempList.sort()
    for j in range(N//K):
        new_list[N//K*i+j]=tempList[j]


print(*new_list)