import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
num = list(map(int, input().rstrip().split()))

max_num = 0

for a in range(0, len(num)-2):
    for b in range (a + 1, len(num)-1):
        for c in range(b + 1, len(num)):
            if num[a] + num[b] + num[c] <= M and num[a] + num[b] + num[c] > max_num:
                max_num = num[a] + num[b] + num[c]

print(max_num)
