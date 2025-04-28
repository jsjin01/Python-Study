import sys
input = sys.stdin.readline

N = int(input().rstrip())
is_existence = False

for n in range (N):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)
    
    if n + sum == N:
        print(n)
        is_existence = True
        break

if(not is_existence):
    print("0")