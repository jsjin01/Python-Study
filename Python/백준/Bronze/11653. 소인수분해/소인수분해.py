import sys
import math
input = sys.stdin.readline

N = int(input().rstrip())

if not N == 1:
    while True:
        found_factor = False
        if N == 1:
            break
        else :
            for i in range(2, int(math.sqrt(N) + 1)):
                if N % i == 0:
                    N = N//i
                    print(i)
                    found_factor = True
                    break   
        if not found_factor:
            print(N)
            break    