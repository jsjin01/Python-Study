import sys
input = sys.stdin.readline

D, K = map(int, input().rstrip().split())

sum_a1 = 0
sum_a2 = 0
number = [[] for _ in range(K)]

number[0].append(1)
number[0].append(0)
number[1].append(0)
number[1].append(1)

for i in range(2, D):
    number[i].append(number[i-2][0] + number[i-1][0])
    number[i].append(number[i-2][1] + number[i-1][1])

for i in range(D):
    sum_a1 += number[i][0]
    sum_a2 += number[i][0]

    
