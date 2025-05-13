import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input().rstrip())
N_array = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
M_array = list(map(int, input().rstrip().split()))

N_array.sort()

for i in M_array:
    if bisect_left(N_array,i) >= N:
        print("0")
    else:
        if i == N_array[bisect_left(N_array,i)] :
            print("1")
        else:
            print("0")