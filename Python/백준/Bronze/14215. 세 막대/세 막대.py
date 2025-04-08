import sys
input = sys.stdin.readline

stick = list(map(int, input().split()))

if max(stick) >= sum(stick) - max(stick):
    print((sum(stick) - max(stick)) * 2 - 1)
else:
    print(sum(stick))