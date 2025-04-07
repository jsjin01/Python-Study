import sys
input = sys.stdin.readline

N,B = map(int, input().rstrip().split())
s = ""
while not N == 0:
    rest = N % B
    N = N // B
    if rest > 9 :
        s += chr(rest + 55)
    else:
        s += str(rest)
    

s = "".join(reversed(s))

print(s)
