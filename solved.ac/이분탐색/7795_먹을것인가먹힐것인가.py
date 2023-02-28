# 내 풀이 252ms
import sys
input = sys.stdin.readline

def binary_search(s, e, B, a):
    res = 0
    while s <= e:
        mid = (s+e)//2
        if B[mid] >= a:            # mid값이 a보다 크거나 같으면 조절
            e = mid-1
        else:
            s = mid+1              # mid값이 a보다 작아지면 res 에 mid값을 담아주고 리턴
            res = mid
    return res+1
    
for _ in range(int(input())):
    N, M = map(int, input().split())             # N = A의 크기, M = B의 크기
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    
    for a in A:
        if a > B[-1]:                           # B의 최댓값보다 a가 크면 M을 더해줌
            cnt += M
        elif a <= B[0]:                         # B의 최솟값보다 a가 작거나 같으면 패스
            continue
        else:                                   # 둘 다 아니면 이분탐색
            cnt += binary_search(0, M-1, B, a)
            
    print(cnt)

# 다른 사람 풀이 144ms
from sys import stdin
from bisect import bisect_left

def solution(A,B):
    answer = 0
    # 이진 탐색 적용
    for a in A:
        answer += bisect_left(B,a)
    return answer

# input
T = int(stdin.readline())
for _ in range(T):
    N, M = map(int,stdin.readline().split())
    A = sorted(list(map(int,stdin.readline().split())))
    B = sorted(list(map(int,stdin.readline().split())))

    # result
    result = solution(A,B)
    print(result)

'''
(1)  bisect_left(list, data): 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지).
(2)  bisect_right(list, data): 리스트에 데이터를 삽입할 가장 오른쪽 인덱스를 찾는 함수(리스트 내 정렬 순서를 유지).
'''