# import sys

# input = sys.stdin.readline

# N = int(input().rstrip())
# count = 0
# while True:
#     if N <= 10:
#         break
#     else:
#         if N//500 >= 1:
#             count += N//500
#             N = N - (N//500)*500
#         elif N//100 >= 1:
#             count += N//100
#             N = N - (N//100)*100
#         elif N//50 >= 1:
#             count += N//50
#             N = N - (N//50)*50
#         elif N//10 >= 1:
#             count += N//10
#             N = N - (N//10)*10

import sys

input = sys.stdin.readline

N = int(input().rstrip())

count = (N//500) + ((N % 500)//100) + ((N % 100)//50)+ ((N % 50)//10)

print(count)
