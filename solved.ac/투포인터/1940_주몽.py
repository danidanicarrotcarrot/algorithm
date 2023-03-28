# 내 풀이 52ms

N = int(input())
M = int(input())
nums = sorted(list(map(int, input().split()))) # 리스트 정렬
cnt, left, right = 0, 0, N-1                   # left, right값 초기화

while right > left:
    n = nums[left] + nums[right]  # left, right를 인덱스로 하는 리스트 원소를 더해줌
    
    if n < M:                     # 값이 M보다 작으면 left +1
        left += 1
    elif n > M:                   # 값이 M보다 크면 right -1
        right -= 1
    else:                         # 값이 M이랑 같으면 카운트 +1, left +1
        cnt += 1
        left += 1

print(cnt)

'''
이런 비슷한 문제 어디서 풀었었는데.. 
아무튼 리스트 정렬 후 left, right를 양 끝 값으로 설정해주고 시작
각 값을 더해주고 M과 비교한 다음 조건에 맞게 left, right 조정해주면 된다
'''