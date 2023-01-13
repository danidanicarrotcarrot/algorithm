# 영화감독 숌

n = int(input())
first = 666
while n != 0: # n이 0아니면 반복
    if '666' in str(first): # 문자열 안에 666이 있으면
        n -= 1 # n 에서 1 빼기
        if n == 0: # n 이 0 이되면 break
            break
    first += 1 # 666에 1씩 계속 더해줌
print(first)       