import sys
input = sys.stdin.readline

case_number = int(input().rstrip())
qdnp =[0,0,0,0]
for case in range(case_number):
    c = int(input().rstrip())
    qdnp[0] = c//25
    c = c % 25
    qdnp[1] = c//10
    c = c % 10
    qdnp[2] = c //5
    c = c % 5
    qdnp[3] = c
    s = ""
    for num in qdnp:
        s += str(num) + " "
    print(s)