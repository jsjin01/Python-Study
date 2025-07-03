import sys
input = sys.stdin.readline

A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())

result = str(A * B * C)

for i in range(0, 10):
    count = 0
    for j in result:
        if i == int(j):
            count += 1
    print(count)