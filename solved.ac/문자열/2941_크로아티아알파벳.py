# 내 풀이(96ms)
import sys
input = sys.stdin.readline

n = sorted([int(input()) for i in range(int(input()))]) # input 받아서 정렬
ans = [(len(n)-idx)*num for idx, num in enumerate(n)]   # 젤 작은 수부터 순서대로 가져와서 리스트 전체 길이 - 인덱스 * 숫자
print(max(ans)) # max 값만 출력

'''
첨엔 걍 단순히 [제일 작은 수 * 로프 개수] 가 답이라고 생각했는데 틀려서 뭐지 하고 다시 읽어봤다
로프를 다 쓰지 않는다는 것이 핵심인둣
[2, 3, 4, 6, 7, 8, 9, 10] 같이 주어지면, 2*8 16 보다는 6*5 30 이 더 크니까
순서대로 정렬한 다음 하나하나 개수랑 곱해주고 그 중에 젤 큰 수가 답일거라 생각했당
풀어서 다행이다.. 
컴프리헨션 파티가 되었다
'''