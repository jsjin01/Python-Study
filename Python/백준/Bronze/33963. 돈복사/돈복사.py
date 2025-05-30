import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = len(str(N))
cnt = 0

for i in range(0,5):
    N *= 2
    if len(str(N)) > l:
        print(cnt)
        break
    cnt += 1