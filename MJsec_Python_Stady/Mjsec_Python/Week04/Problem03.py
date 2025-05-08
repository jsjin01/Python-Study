import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input().rstrip())
N_arr = list(map(int, input().rstrip().split()))

M = int(input().rstrip())
M_arr = list(map(int, input().rstrip().split()))

N_arr.sort()

R_arr = []

for i in M_arr:
    print(f"{bisect_right(N_arr,i)-bisect_left(N_arr,i)}", end =" ")
# 개행 문자열 제거

# for i in M_arr:
#     R_arr.append(bisect_right(N_arr,i)-bisect_left(N_arr,i))

# ps =""
# for s in R_arr: 
#     ps += str(s) + " "