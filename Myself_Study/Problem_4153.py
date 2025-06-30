import sys
input = sys.stdin.readline

while True:
    ar = list(map(int, input().rstrip().split()))
    if ar[0] == 0 & ar[1] == 0 & ar[2] == 0:
        break
    big_num = max(ar)
    ar.remove(big_num)
    if pow(big_num,2) ==pow(ar[0],2) + pow(ar[1],2):
        print("right")
    else:
        print("wrong")