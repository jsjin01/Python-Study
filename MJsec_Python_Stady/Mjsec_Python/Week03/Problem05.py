import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for i in range(N):
    n = int(input().rstrip())
    arr.append(n)

# ##시간 초과 sort가 시간을 엄청 잡아먹기 때문에

# sum = 0
# while(len(arr) != 1):
#     arr.sort()
#     sum += arr[0]+arr[1]
#     arr.append(arr[0]+arr[1])
#     arr = arr[2:]

# print(sum)

##해결하기 위해서는 heap 정렬을 사용해야됨
##heapq는 리스트에서 조작함
heapq.heapify(arr)

sum = 0

while(len(arr) > 1):
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    sum += x + y
    heapq.heappush(arr,x+y)

print(sum)