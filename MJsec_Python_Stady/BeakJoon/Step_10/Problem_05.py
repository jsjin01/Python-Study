import sys
input = sys.stdin.readline

input_number = int(input().rstrip())
dots_list = [[0,0] for i in range(input_number)]

for i in range(input_number):
    dots_list[i] = list(map(int, input().rstrip().split()))

x_min = 10000
x_max = -10000
y_min = 10000
y_max = -10000

for i in range(input_number):
    if x_min > dots_list[i][0]:
        x_min = dots_list[i][0]

    if x_max < dots_list[i][0]:
        x_max = dots_list[i][0]
    
    if y_min > dots_list[i][1]:
        y_min = dots_list[i][1]
    if y_max < dots_list[i][1]:
        y_max = dots_list[i][1]

print((x_max-x_min)*(y_max-y_min))