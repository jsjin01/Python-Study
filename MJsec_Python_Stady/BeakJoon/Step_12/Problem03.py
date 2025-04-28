import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().rstrip().split())

den = a*e - b*d

x = (c*e - b*f) // den
y = (a*f - c*d) // den

print(f"{(x)} {(y)}")