import sys
import queue
input = sys.stdin.readline

## 속도 때문에
console_num = int(input().rstrip())
q = queue.Queue()

for i in range (console_num):
 
    text = input().rstrip()
    if(text[0:4] == "push"):
        q.put(int(text[5:]))
    elif(text[0:3] == "pop"):
        if not q.qsize() == 0:
            print(q.queue[0])
            q.get()
        else:
            print("-1")
    elif(text[0:5] =="front"):
        if not q.qsize() == 0:
            print(q.queue[0])
        else:
            print("-1")
    elif(text[0:5] =="back"):
        if not q.qsize() == 0:
            print(q.queue[-1])
        else:
            print("-1")
    elif(text[0:4] == "size"):
        if not q.qsize() == 0:
            print(q.qsize())
        else:
            print("0")
    elif(text[0:5] =="empty"):
        if q.qsize() == 0 :
            print("1")
        else:
            print("0")