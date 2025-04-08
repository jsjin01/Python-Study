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
                    ##소수로 나눌 수 있는지 판단
                    found_factor = True
                    break
                #나눌 수 없으면 탈출   
        if not found_factor:
            print(N)
            break        