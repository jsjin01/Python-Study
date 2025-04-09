import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

print(int(A) + int(B) - int(C))
print(int(str(A) + str(B)) - int(C))