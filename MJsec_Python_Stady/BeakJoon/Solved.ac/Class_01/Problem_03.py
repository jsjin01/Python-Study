import sys
input = sys.stdin.readline

number_array = list(map(int, input().split()))

result = 0

for n in number_array:
    result += n**2

print(result%10)