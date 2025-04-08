import sys
import math
input = sys.stdin.readline

M = int(input().rstrip())
N = int(input().rstrip())
d_list = []

for n in range(M,N+1):
    d = 0
    if n > 1:   
        for i in range (2, int(math.sqrt(n))+1):
            if n % i == 0:
                d += 1
    else:
        continue
    
    if d == 0:
        d_list.append(n)

if not len(d_list) == 0:
    sum = 0
    for i in d_list:
        sum += i
    print(sum)
    print(min(d_list))
else:
    print("-1")