import sys
input = sys.stdin.readline

N = int(input().rstrip())


# 포함되는 행 구하기
start_num = 2
line = 0
if not N == 1:
    for i in range(N):
        if start_num <= N < start_num + (i+2):
            line = i + 2
            inline_number = N- start_num
            break
        start_num = start_num + (i+2)
    
    if line % 2 == 0:
        print(str(1 + inline_number)+"/"+str(line - inline_number))
    else:
        print(str(line - inline_number)+"/"+str(1 + inline_number))
else:
    print("1/1")

