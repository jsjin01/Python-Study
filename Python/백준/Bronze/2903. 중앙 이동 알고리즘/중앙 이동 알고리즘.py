import sys
input = sys.stdin.readline


N = int(input().rstrip())
init_dots = 2

for k in range(N):
    init_dots += (init_dots-1)

print(init_dots*init_dots)