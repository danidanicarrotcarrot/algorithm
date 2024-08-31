# 칸토어 집합

## 예전 풀이 [Finished in 69ms]
import sys
for i in sys.stdin:
	temp = '-'
	for j in range(int(i)):
		temp = temp+' '*len(temp)+temp
		# print(j, temp)
	print(temp)

## 재귀함수 이용 [Finished in 668ms]
def func(k):
	# base case
	if k == 0:
		return '-'
	# recursive case
	return func(k-1)+(' '*(3**(k-1)))+func(k-1)

while True:
	try:
		n = int(input())
		print(func(n))
	except:
		break
