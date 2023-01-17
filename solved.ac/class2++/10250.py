# ACM 호텔

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    hotel_num = [] # 그냥 호수 순서대로 리스트 생성해버림

    for i in range(1, w+1):
        for j in range(1, h+1):
            hotel_num.append(i + (j*100))

    print(hotel_num[n-1]) # 인덱스 번호로 출력

# 다 도니까 리스트 만드는데 오래걸릴듯 .. 썩 좋은 방법은 아니라고 생각함 ㅠ