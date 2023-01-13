# 내 풀이 (2020ms)
from collections import deque

N,K = map(int, input().split())
y = deque(i for i in range(1, N+1))    # 큐 만들어주고 1~n만큼 숫자 넣어줌
ans = []                               # 정답용 리스트

while y:                               # 큐가 빌 때까지 반복
    for _ in range(K-1):               # K - 1 만큼 반복하면서 왼쪽에서 빼서 오른쪽에 추가
        y.append(y.popleft())          
    ans.append(y.popleft())            # K번째 수는 빼서 ans에 추가

print(str(ans).replace('[', '<').replace(']', '>')) # ans 리턴

'''
벼락치기 중이라 다른 사람 풀이는 못 가져왔어용..
암튼 그냥 리스트로 했더니 시간초과 나서 deque 썼더니 되더라 ~~~
+ replace로 괄호 쉽게 바꾸는 방법 get
'''