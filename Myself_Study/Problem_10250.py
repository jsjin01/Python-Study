import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    H, W ,N = map(int, input().rstrip().split())
    if H ==0 :
        h = H
        w = H // N
    else:
        #거리
        w = N // H + 1
        #층수
        h = N % H
    if w < 10:
        w = "0"+str(w)
    s = str(h)+w
    print(s)

