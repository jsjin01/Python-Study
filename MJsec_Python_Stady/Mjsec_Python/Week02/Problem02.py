import sys

input = sys.stdin.readline

S = input().rstrip()

# 11001011
count = 0
c = S[0]
front_s = S[0]

for s in S:
    if s != c and s != front_s:
        count += 1
        front_s = s
    elif s == c and s != front_s:
        front_s = s
    
print(count)


# One = [i for i in s.split("0") if i =""]
# Zero = [i for i in s.split("1") if i =""]
# print(min(len(One), len(Zero)))