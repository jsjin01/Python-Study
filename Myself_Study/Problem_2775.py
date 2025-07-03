import sys
input = sys.stdin.readline
#
# 2 1 4 10
# 1 1 3 6
# 0 1 2 3

T = int(input().rstrip())

for _ in range(T):
    k = int(input().rstrip())  # 층
    n = int(input().rstrip())  # 호 

    apt = [[0]* (n + 1) for _ in range(k+1)]

    for i in range(1, n+1):
        apt[0][i] = i
    
    for floor in range(1,k+1):
        for room in range(1, n+1):
            apt[floor][room] = apt[floor][room - 1] + apt[floor-1][room]
    
    print(apt[k][n])
    