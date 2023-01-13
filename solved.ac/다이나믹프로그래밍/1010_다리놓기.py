# 내 풀이

def factorial(n):                   # 팩토리얼 구현
    if n > 1:
        return n*factorial(n-1)     # n이 1보다 크면 n*fac(n-1) 
    else:
        return 1                    # 그 이하는 1 반환

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m)//(factorial(m-n)*factorial(n)))  # 조합 공식 그대로 n!/((n-r)!*r!)

--------------------------------------------------------------------------------------

# 다른 풀이

dp = [[1] * 31 for _ in range(31)]                  # 배열 미리 30*30으로 세팅
for i in range(31):                                 # 첫번째 열은 1~30까지 순서대로 
    dp[1][i] = i
for i in range(2, 31):                              # 두번째부터는 규칙대로
    for j in range(i + 1, 31):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])                                  # n, m 번째 출력

'''
이게 뭐야 하고 한참 보다가 조합인 거 같아서 조합으로 풀었다
dp로 푸는 방법도 생각해봤지만 나에겐 너무 어려웠다고 한다..
다른 풀이 찾아보면서 dp 방식도 이해할 수 있어서 좋았다 ㅎㅎ 다음엔 dp로 꼭 풀 수 있도록 ..
'''