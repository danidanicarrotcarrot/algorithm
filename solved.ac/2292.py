# 벌집

n = int(input())
cnt = 1
cnt_room = 1

while n > cnt_room:
    cnt_room += cnt * 6
    cnt += 1

print(cnt)