import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = [list(map(int, input().split())) for i in range(n)]
time = sys.maxsize                      # 최대 정수값
floor = 0

for x in range(257):                    # 0층부터 256층까지 반복하여 블록을 확인
    remove_block, add_block = 0, 0      # remove -> 블록 제거 작업 / add -> 블록 추가 작업

    for i in range(n):
        for j in range(m):
        
            if ground[i][j] < x:        # 블록 < 층수 -> add_block에 더해줌
                add_block += x - ground[i][j]
            else:                       # 블록 > 층수 -> remove_block에 더해줌
                remove_block += ground[i][j] - x
        
    if remove_block+b >= add_block:     # remove + b > add 일 때만 작업 가능
        if remove_block*2 + add_block <= time:
            time = remove_block*2 + add_block
            floor = x                   # 작업 가능할때만, 시간이랑 층 구해서 업뎃시켜줌
                                        # 0부터 256층까지 비교하므로 업데이트될수록 고층의 최저 시간임

print(time, floor)