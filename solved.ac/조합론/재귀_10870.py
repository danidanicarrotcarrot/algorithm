# n번째 피보나치 수를 구하는 문제

n = int(input())


## 1. 반복문 + 메모이제이션
# n = int(input())

# arr = [-1] * (n + 2)
# arr[0] = 0
# arr[1] = 1

# for i in range(2, n + 1):
# 	arr[i] = arr[i-1] + arr[i-2]

# print(arr[n])

## 2. 재귀함수 사용
# def fibo(n):
# 	if n == 0:
# 		return 0
# 	if n == 1:
# 		return 1
# 	return fibo(n-1)+fibo(n-2)
# print(fibo(n))

## 3. 재귀 + 메모이제이션 > 반복되는 연산을 줄여줌
def fibo(x):
	global arr

	if arr[x] != -1:
		return arr[x]

	arr[x] = fibo(x-1) + fibo(x-2)
	return arr[x]

arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1

print(fibo(n))