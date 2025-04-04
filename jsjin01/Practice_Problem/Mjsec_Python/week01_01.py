import sys
input = sys.stdin.readline

## 속도 때문에
console_num = int(input().rstrip())
storege = []

for i in range (console_num):
 
    text = input().rstrip()
    if(text[0:4] == "push"):
        storege.append(text[5:])
    elif(text[0:3] == "pop"):
        if not len(storege) == 0:
            print(storege[-1])
            storege.pop()
        else:
            print("-1")
    elif(text[0:3] =="top"):
        if not len(storege) == 0:
            print(storege[-1])
        else:
            print("-1")
    elif(text[0:4] == "size"):
        if not len(storege) == 0:
            print(len(storege))
        else:
            print("0")
    elif(text[0:5] =="empty"):
        if len(storege) == 0 :
            print("1")
        else:
            print("0")
    