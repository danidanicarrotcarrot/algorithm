import sys
input = sys.stdin.readline

words = {}
for i in range(int(input())):
    x = input().strip()
    words[x] = len(x)

words = words.items()
words = sorted(words, key = lambda x: (x[1], x[0]))

for w in words:
    print(w[0])