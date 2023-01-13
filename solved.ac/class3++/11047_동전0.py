# 내 풀이 30616	36ms
N, K = map(int, input().split())
coin = sorted([int(input()) for _ in range(N)], reverse = True) # 내림차순 정렬

cnt = 0
for i in coin:        # i가 K보다 작을때 cnt는 i로 나눈 몫을 더하고, K는 나머지로 없데이트
    if K < 0:
        break
    elif i > K:
        continue
    else:
        cnt += K//i
        K = K%i
print(cnt)

# 다른 사람 풀이 30616	44ms
N, K = map(int, input().split()) 
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복
print(count)

'''
비슷비슷한 풀이법 ..
쉽당 쉬워
'''