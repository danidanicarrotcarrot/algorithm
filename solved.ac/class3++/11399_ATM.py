# 내 풀이 30616	44ms

N = int(input())                         
P = sorted(map(int, input().split()))   # 받아서 순서대로 정렬

p = 0
for i in range(N):                      # 사람 수만큼 반복
    p += sum(P[:i+1])                   # 슬라이싱으로 i+1번째까지 더한 값을 p에 추가

print(p)

'''
쉬웠당
'''