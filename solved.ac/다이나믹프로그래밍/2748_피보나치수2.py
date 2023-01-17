# 시간초과

def fibo(n):
    if n == 0 or n == 1:          # 0과 1이면 그대로 반환
        return n
    return fibo(n-1) + fibo(n-2)  # 점화식 그대로
    
n = int(input())
print(fibo(n))

------------------------------------------------------------

# 다른 풀이 (80ms)

fibo = []                          # 피보나치 리스트
fibo.append(0)                     # 0과 1 추가
fibo.append(1)

for i in range(2, int(input())+1):     # 2부터 n 까지
    fibo.append(fibo[i-1]+fibo[i-2])   # 피보나치 수를 리스트에 추가

print(fibo[-1])                    # 맨 마지막 수 출력

'''
시간초과 ㅠㅡㅜ 나서 다른 방법으로 해봤다
저만 DP로 안 했군요?.. 
'''