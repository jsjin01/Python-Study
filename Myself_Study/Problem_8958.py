import sys
input = sys.stdin.readline

N = int(input().rstrip())

for _ in range(N):
    s = input().rstrip()
    n_sum = 0
    count = 0
    for c in s:
        if c == "O":
            count += 1
            n_sum += count
        else:
            count = 0
    print(n_sum)
