import sys
input = sys.stdin.read

n, r = map(int, input().rstrip().split())

def factorial(N):
    num = 1
    for i in range(1,N+1):
        num *= i
    
    return num
    

c = factorial(n)/(factorial(r)*factorial(n-r))
print(int(c))