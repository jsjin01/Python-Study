import sys
input = sys.stdin.readline
##중앙값을 찾으면 됨
N = int(input().rstrip())
house_array = list(map(int, input().rstrip().split()))
house_array.sort()

print(house_array[(N-1)//2])

