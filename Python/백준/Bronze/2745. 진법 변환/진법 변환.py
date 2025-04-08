import sys
input = sys.stdin.readline

def Change_Number(s: str, n: int ):
    sum = 0
    s = "".join(reversed(s))
    for i in range (len(s)):
        if (ord(s[i]) >= 65) and (ord(s[i]) <= 90):
            if(i == 0):
                sum += ord(s[i]) - 55
            else:      
                sum += n**(i)* (ord(s[i]) - 55)
        else:
            if(i == 0):
                sum += int(s[i])
            else:      
                sum += n ** (i)* int(s[i])
    return sum

## 속도 때문에


N, B = map(str ,input().rstrip().split())
print(Change_Number(N,int(B)))