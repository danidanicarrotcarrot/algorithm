# 내 풀이
def solution(n):
    ans = 0
    for i in range(2, n+1):
        for j in range(2, int(i**(0.5))+1):
            if not i%j:
                break
        else:
            ans += 1
    return ans

# 다른 사람 풀이
def solution(n):
    num=set(range(2,n+1))         

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

'''
for - else 로 소수만 찾아서 + 1
처음에 제곱근으로 안 했더니 몇 개는 시간초과가 떴당 
소수는 ? 제곱근까지만 찾자
'''