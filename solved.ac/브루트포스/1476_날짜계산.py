# 내 풀이
E, S, M = map(int, input().split())
e, s, m, cnt = 0, 0, 0, 1

while True:
    e += 1
    s += 1
    m += 1
    
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1

    if e == E and s == S and m == M:
        break
    cnt += 1
    
print(cnt)

'''
ㅎㅎ 어려워보였는데 이해하니까 간단했다..
브루트포스는 풀이방법이 다 비슷한 것 같아서 다른 풀이는 가져오지 않겠당! -> ?
'''