import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
N_len = list(map(int,input().rstrip().split()))

max_l = max(N_len)
min_l = 0
lenght = 0

while min_l <= max_l:
    mid = (max_l + min_l) // 2
    len_cnt = sum(l - mid for l in N_len if l - mid >= 0)
    if len_cnt >= M:
        lenght = mid
        min_l = mid + 1
    else :
        max_l = mid - 1

print(lenght)