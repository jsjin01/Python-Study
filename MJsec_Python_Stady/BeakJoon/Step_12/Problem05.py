import sys
input = sys.stdin.readline

N = int(input().rstrip())

cnt = 0
for i in range (666*10000):
    if "666" in str(i):
        cnt += 1
        if cnt == N:
            print(i)
            break