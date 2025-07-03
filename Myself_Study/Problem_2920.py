import sys
input = sys.stdin.readline

i = input().rstrip()

if i == "1 2 3 4 5 6 7 8":
    print("ascending")
elif i == "8 7 6 5 4 3 2 1":
    print("descending")
else:
    print("mixed")
