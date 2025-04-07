import sys
input = sys.stdin.readline

#규칙성
# 1         => 1
# 2 7 /5    =>2
# 8 19 /11  =>3
# 20 37 /17 =>4
# 38 61 / 23=>5

N = int(input().rstrip())
count = 0
start_number = 2


for i in range (N):
    if N == 1:
        count = 1
        break
    
    if start_number <= N and  N < start_number + 6 *(i+1):
        count = i + 2
        break
    
    start_number = start_number + 6 *(i+1)

print(count)
