import sys
input = sys.stdin.readline

N = int(input().rstrip())
min_count = float("inf")

for five in range(0, N//3 +1):
    for three in range(0, N//3 +1):
        if N == five*5 +three*3 :
            count  = five + three
            min_count = min(count,min_count)

if min_count ==float("inf"):
    print("-1")
else:
    print(min_count)

