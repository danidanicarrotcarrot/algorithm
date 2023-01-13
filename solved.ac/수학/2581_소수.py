# 내 풀이

M = int(input())
N = int(input())

ans = []
for i in range(M, N+1):   
    if i == 1 :              # 1은 소수가 아니라서 건너뛰기
        continue
    for j in range(2, i):    # 2부터 i-1까지 나눠보기 나누어 떨어지면 소수가 아니라서 break
        if i%j == 0:
            break
    else: 
        ans.append(i)        # for - else로 소수만 ans에 추가
        
print(sum(ans), ans[0], sep='\n') if ans else print(-1)

'''
처음에 1을 처리 안해줘서 틀렸음
그래도 풀어서 다행이당
'''