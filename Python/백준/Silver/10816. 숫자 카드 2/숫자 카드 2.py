import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input().rstrip())
N_array = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
M_array = list(map(int, input().rstrip().split()))

N_array.sort()

for n in M_array:
    print(f"{bisect_right(N_array, n) - bisect_left(N_array, n)}", end= " ")