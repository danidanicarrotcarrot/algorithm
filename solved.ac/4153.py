# 직각삼각형

while True:
    data = list(map(int, input().split()))
    if data[0] == 0: # 반복문 탈출 -> 0 0 0 나오기 전에는 다 양의 정수임
        break
    data.sort() # 정렬
    x = [i**2 for i in data] # 제곱
    print('right') if x[-1] == x[-2] + x[-3] else print('wrong') # if - else 한 줄로 