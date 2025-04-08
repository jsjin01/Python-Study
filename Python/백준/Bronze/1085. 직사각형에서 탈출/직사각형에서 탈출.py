import sys
input = sys.stdin.readline

x, y, w, h  = map(int,input().rstrip().split())

w_to_x = w - x
h_to_y = h - y

l_list = [x, y, w_to_x, h_to_y]

print(min(l_list))