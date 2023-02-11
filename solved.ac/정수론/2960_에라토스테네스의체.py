# 내 풀이 56ms
n, k = map(int, input().split())

nums = []                       # 제거한 정수
cnt = 0                         # 제거 횟수 카운트

for i in range(2, n+1):         # 2 ~ n
    
    for j in range(1, n//i+1):  # 1 ~ n//i
        
        if cnt == k:            # 제거 횟수 = k 면 break
            break
            
        if j*i not in nums:     # i*j가 이미 제거되지 않은 경우에만 append
            nums.append(j*i)
            cnt += 1            # 제거 횟수 카운트 + 1

print(nums[-1])

'''
for 문 돌면서 제거한 정수 nums에 추가 + 횟수 카운트
제거 횟수 = k 인 지점에서 전체 for문 종료
리스트 마지막 인덱스 꺼내서 출력

break 지점을 처음에 잘못 잡아서 실패 나왔었다..
테스트케이스 여러개 넣어보고 수정 후 제출 완료 ~!
'''