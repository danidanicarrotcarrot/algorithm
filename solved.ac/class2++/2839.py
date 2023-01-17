# 설탕 배달

n = int(input())

cnt = 0 

if n%5 == 0: # 5의 배수일경우
    print(n//5)
else:
    while n > 0:
        n -= 3
        cnt += 1
        if n%5 == 0: # 3과 5의 조합으로 되는 경우
            cnt += n//5
            print(cnt)
            break
        elif n == 1 or n == 2: # 안되는 경우
            print(-1)
            break
        elif n == 0: # 3으로만 되는 경우
            print(cnt)
            break