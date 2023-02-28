# 내 풀이 44ms
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
Z = Y*100//X                            # 승률

if Z >= 99:                             # 100으로 하면 틀림 .. why?
    print(-1)
else:                                   
    l, r, ans = 1, X, 0                 # 시작과 끝 지점, ans 값 지정
    while l <= r :                      
        mid = (l+r)//2                  # 중간 값 지정
        if (Y+mid)*100//(X+mid) <= Z:   # mid를 더한 승률이 기존 승률보다 작거나 같으면 left 값을 right보다 크게 만들어줌 -> 반복문 종료
            l = mid + 1
        else:                           # 새로운 승률이 기존 승률보다 크면 right 값을 mid -1 로 해줌
            ans = mid                   # ans에는 매번 mid 값을 넣어줌
            r = mid - 1
    print(ans)                          # 마지막에 담은 ans값 출력

'''
처음엔 그냥 x, y에 +1을 해주면서 승률이 달라지는 지점을 찾았는데 시간초과나서 이분탐색으로 풀었다
이런 문제는 보자마자 바로 풀 수 있을 정도로 알고리즘을 외워두어야 할 것 같다
로직은 다 비슷비슷한 듯 ..!!
'''