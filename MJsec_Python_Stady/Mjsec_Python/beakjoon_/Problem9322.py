import sys
input = sys.stdin.readline

N = int(input().rstrip())

for i in range(N):
    num = int(input().rstrip())
    s = ["" for _ in range(num)]
    one = list(map(str, input().rstrip().split()))
    two = list(map(str, input().rstrip().split()))
    three = list(map(str, input().rstrip().split()))
    for i in range (num):
        s[one.index(two[i])] = three[i]
    
    for k in s:
        print(k,end=" ")
    print()