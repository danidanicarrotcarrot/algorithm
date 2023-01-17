# 분해합

n = int(input())

for m in range(1, n+1): # 1 부터 n+1까지 모든 경우의 수 탐색
    nums = sum(map(int, str(m))) # m 각 자릿수의 합
    if nums + m == n : # m + nums = n 이면 생성자 m 출력
        print(m)
        break
    if m == n : print(0) # m 과 n 이 같아지는 경우 (생성자가 없는 경우) 0 출력

# 브루트포스 알고리즘 문제 (완전 탐색법, 무차별 대입법)
# 가능한 모든 경우의 수 탐색 