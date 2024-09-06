# 그리디_5585.py
# 거스름돈 / 브론즈 2


## 내 풀이
N = int(input()) # 물건의 금액

change = 1000-N  # 잔돈

coins = {500:0, 100:0, 50:0, 10:0, 5:0, 1:0}

for i in coins: # 500, 100, ...
	coins[i] += change//i  # 잔돈을 코인으로 나눈 몫
	if change % i == 0:	   # 잔돈이 0이 되면 stop
		break
	change %= i            # 잔돈은 나머지로 세팅

print(sum(coins.values())) # 각 value의 합


## 더 깔끔한 풀이
money = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    cnt += money // coin
    money %= coin

print(cnt)

