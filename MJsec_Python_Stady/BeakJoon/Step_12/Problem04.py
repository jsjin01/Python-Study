import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
input_array = [""]*N
min_number = float("inf")

for input_index in range(N):
    input_array[input_index] = input().rstrip()

for x in range(N-7):
    for y in range(M-7):
        point = ""
        count = 0
        for N_index in range(x, x+8):
            if (N_index - x)%2 == 1:
                point = "B"
            else:
                point = "W"
            for M_index in range(y, y+8):
                if input_array[N_index][M_index] != point:
                    count +=1
                if point =="B":
                    point = "W"
                else:
                    point ="B"

        min_number = min(min_number, count)
        count = 0
        for N_index in range(x, x+8):
            if (N_index- x)%2 == 1:
                point = "W"
            else:
                point = "B"
            for M_index in range(y, y+8):
                if input_array[N_index][M_index] != point:
                    count +=1
                if point =="B":
                    point = "W"
                else:
                    point ="B"
        min_number= min(min_number, count)

print(min_number)