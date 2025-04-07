import sys
input = sys.stdin.readline

while True:
    N = int(input().rstrip())
    sum = 1
    divisor_list = []

    if N == -1:
        break

    for i in range(2, N):
        if N % i == 0:
            divisor_list.append(i)

    for num in divisor_list:
        sum += num
    
    if(N == sum):
        s = str(N) + " = 1"
        for n in divisor_list:
            s += " + " + str(n)
        print(s)
    else:
        print(f"{N} is NOT perfect.")