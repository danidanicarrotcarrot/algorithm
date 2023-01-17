# Hashing

l = int(input())
num = [ord(i)-96 for i in input()]

hash = 0

for j in range(l):
    hash += num[j]*(31**j)

print(hash%1234567891)