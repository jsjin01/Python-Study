import sys
input = sys.stdin.readline

def Dict_in(n : int, d : dict):
    if not n in d:
        d[n] = 1
    else:
        d[n] += 1

one_bot = list(map(int, input().rstrip().split()))
two_bot = list(map(int, input().rstrip().split()))
three_bot = list(map(int, input().rstrip().split()))

x_Dict = {}
y_Dict = {}

x_Dict[one_bot[0]] = 1
y_Dict[one_bot[1]] = 1

Dict_in(two_bot[0], x_Dict)
Dict_in(two_bot[1], y_Dict)
Dict_in(three_bot[0], x_Dict)
Dict_in(three_bot[1], y_Dict)

s = ""
for k in x_Dict.keys():
    if(x_Dict[k] == 1):
        s += str(k)
s += " "
for k in y_Dict.keys():
    if(y_Dict[k] == 1):
        s += str(k)

print(s)






