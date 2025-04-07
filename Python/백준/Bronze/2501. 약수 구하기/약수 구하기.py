import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

divisor_list = []

for i in range(1, N+1):
    if N % i == 0:
        divisor_list.append(i)

if len(divisor_list) >= K:
    print(divisor_list[K-1])
else:
    print(0)
