import sys
input = sys.stdin.readline

while True:
    A , B = map(int, input().rstrip().split())
    if A == 0 and B == 0:
        break
    elif B % A == 0 and B // A > 1:
        print("factor")
    elif A % B == 0 and A // B > 1:
        print("multiple")
    else:
        print("neither")