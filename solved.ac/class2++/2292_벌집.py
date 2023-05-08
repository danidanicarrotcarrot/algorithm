n = int(input())

cnt = 1
room = 1

while n > room:
    room += 6*cnt
    cnt += 1
    
print(cnt)