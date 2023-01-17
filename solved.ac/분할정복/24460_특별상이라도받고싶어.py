# 내 풀이 692ms -> 답지 참고

def devide(x, y, n):
    if n == 1:
        return graph[x][y]                              
    else:
        res = [
            devide(x, y, n // 2),                      # 0,0,1 
            devide(x, y + n // 2, n // 2),             # 0,1,1
            devide(x + n // 2, y, n // 2),             # 1,0,1
            devide(x + n // 2, y + n // 2, n // 2)     # 1,1,1
        ]
        return sorted(res)[1]


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
print(devide(0, 0, N))

'''
분할정복을 드디어 조금은 알 것 같다 ㅠㅠ
처음엔 답지를 봐도 이해를 못해서 포기했었는데 어제 명강의를 듣고 조금은 깨우친둣
이제 답지가 이해가 된다 ....!! 꺄 다음엔 제대로 풀어봐야지
'''