# 카드 2

# card = [i for i in range(1, int(input())+1)]

# for _ in range(len(card)):
#     if len(card) == 1:
#         print(card[0])
#     else:
#         card.pop(0)    
#         card.append(card[0])
#         card.pop(0)

from collections import deque

queue = deque([i for i in range(1, int(input())+1)])

for _ in range(len(queue)):
    if len(queue) == 1:
        print(queue[0])
    else:
        queue.popleft()
        queue.append(queue[0])
        queue.popleft()
        