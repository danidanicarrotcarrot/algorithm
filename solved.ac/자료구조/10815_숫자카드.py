# 내 풀이 (680ms)
_ = int(input())
N = set(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))

for i in M:
    if i in N:
        print(1, end=' ')
    else:
        print(0, end=' ')

'''
end = '' 로 해서 자꾸 틀렸습니다 떠서 빡쳤당
출력도 잘 확인하자
첨에 list로 통일했더니 시간초과 나서 저번에 set이 찾는거 빠르다고 했던게 기억나서 썼음
'''