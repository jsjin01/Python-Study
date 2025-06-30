import sys
input = sys.stdin.readline

while True:       
    N = int(input().rstrip())

    if N != 0:
        s= str(N)
        if len(s) == 1:
            print("yes")
        else:
            if len(s) % 2 == 1:
                if s[0:len(s) // 2] ==  s[-1:len(s) // 2 : -1]:
                    print("yes")
                else:
                    print("no")
            else:
                if s[0 : len(s)//2] == s[-1:len(s)//2 -1:-1]:
                    print("yes")
                else:
                    print("no")
    else:
        break