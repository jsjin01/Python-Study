import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

m = 0
n = a*b
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        m = max(m,i)

#최소 공약수 구하는 식
n = a * b // m

print(m)
print(n)