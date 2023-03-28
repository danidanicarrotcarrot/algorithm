# 내 풀이 3184ms

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())   # 초밥 수 N, 초밥 메뉴 d, 연속 접시 개수 k, 쿠폰 번호 c
nums = [int(input()) for i in range(N)]               # 회전초밥 리스트 nums
nums = nums + nums[:k]                                # k 만큼 리스트 추가
susui = [len(set(nums[i:i+k]+[c])) for i in range(N)] # [i:i+k]만큼 리스트 슬라이싱, 쿠폰번호 추가, set으로 중복 제거  
print(max(susui))                        # 먹을 수 있는 초밥 가짓수 중 max 값

'''
k개씩 연속되게 리스트를 자름 + 쿠폰번호 c 추가 -> set(중복 제거) -> 먹을 수 있는 초밥 가짓수가 나옴
len으로 초밥 리스트의 길이만 담아주고, max값 출력 

[{9, 30, 7}, {9, 2, 30, 7}, {2, 30, 7}, {9, 2, 30, 7}, **{2, 7, 9, 25, 30}**, {9, 30, 25, 7}, {9, 30, 25, 7}, {25, 30, 9, 7}]
[3, 4, 3, 4, **5**, 4, 4, 4] -> 5 출력
'''