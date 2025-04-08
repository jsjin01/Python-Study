import sys
input = sys.stdin.readline

N = int(input().rstrip())

N_list = list(map(int, input().rstrip().split()))
count = 0

for n in N_list:
    d = 0
    if n > 1:   
        for i in range (2, n):
            if n % i == 0:
                d += 1
    else:
        continue
    
    if d == 0:
        count += 1

print(count)