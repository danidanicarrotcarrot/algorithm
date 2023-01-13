# 다현쓰 풀이 68ms

first = int(input())  # input
n = first  # first 변수는 사이클 다 돌았는지 비교해야해서 냄겨둠
i = 1  # 사이클 측정할 변수

while True:
    if n < 10:  # n 이 10보다 작으면
        n = '0' + str(n)  # 문자열로 변환해서 앞에 0을 붙여준다

    num = sum(map(int, str(n)))  # map으로 n 각각의 인덱스를 int로 변환해서 sum
    new = int(str(n)[-1] + str(num)[-1])  # n의 마지막 인덱스 + num의 마지막 인덱스 = new

    if new == first:  # 새로운 숫자 new = first 면 스탑
        print(i)  # 사이클 i 출력
        break

    i += 1  # 아니라면 i에 1추가
    n = new  # n = new가 돼서 다시 while문 반복

# 다른 사람 풀이

n = int(input())  # int형태로 input 26이라 치면
num = n
cnt = 0  # 사이클 측정 변수

while True:
    a = num // 10  # 26을 10으로 나눈 몫 / 즉 10의 자리 숫자 2
    b = num % 10  # 26을 10으로 나눈 나머지 / 즉 1의 자리 숫자 6
    c = (a + b) % 10  # 2+6 8을 10으로 나눈 나머지 / 8
    num = (b * 10) + c  # b에 10을 곱한 다음 c 더해줌 = 60 + 8 / 새로운 숫자 68

    cnt = cnt + 1  # 사이클 1 추가
    if num == n:  # num = n 이면 스탑
        break

print(cnt)  # 사이클 출력
