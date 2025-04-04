import sys
from collections import deque
input = sys.stdin.readline

input_num = int(input().rstrip())

for i in range(input_num):

    dq = deque()
    is_reverse = False
    errer = False

    case_part =  input().rstrip()
    case_num = int(input().rstrip())
    case_temp= list(input().rstrip()[1:-1].split(","))
    case_array = list()

# 리스트 받아서 []없애기
    if not case_num == 0:
        for i in range(0, case_num):
            case_array.append(case_temp[i])
    
    for l in case_array:
        dq.append(l)

    for c in case_part:
        if c == "R" :
            is_reverse = not is_reverse
        elif c == "D":
            if not len(dq) == 0 :
                if is_reverse == False:
                    dq.popleft()
                else:
                    dq.pop()
            else:
                print("error")
                errer = True
                break
        
    s = ""
    if not len(dq) == 0:
        if is_reverse :
            dq.reverse()
        s += "["
        for c in dq:
            s += c +","
        
        s = s[:-1]
        s += "]"
        print(s)
    elif not errer:
        print("[]")