import sys
from collections import deque
input = sys.stdin.readline

dq = deque()
dq.reverse()
case_num = int(input().rstrip())

for i in range(case_num):
    case_part =  input().rstrip()
    input_num = int(input().rstrip())
    input_text =  input().rstrip()
    input_text.removeprefix("[")
    input_text.removesuffix("]")
    input_array : list = input_text.split(",")
    for a in input_array:
        dq.append(a)

    for c in case_part:
        if c == "R":
            if not len(dq) == 0:
                dq.reverse()
            else:
                print("errer")
                break
        elif c == "D":
            if not len(dq) == 0:
                dq.popleft()
            else:
                print("errer")
                break


    if not len(dq) == 0: 
        print(dq)
