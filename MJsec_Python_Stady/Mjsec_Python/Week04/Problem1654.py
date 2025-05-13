import sys
input = sys.stdin.readline

K, N = map(int,input().rstrip().split())

K_len = [int(input().rstrip()) for _ in range(K)]

max_len = sum(K_len) // N
min_len = 1
length = 0

##이진 탐색으로 풀어야됨
while min_len <= max_len:
    mid = (min_len + max_len) // 2
    cnt = sum(l // mid for l in K_len)
    if cnt >= N :
        length = mid
        min_len = mid + 1
    else:
        max_len = mid - 1

print(length)