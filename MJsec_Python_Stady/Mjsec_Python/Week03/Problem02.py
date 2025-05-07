import sys
input = sys.stdin.readline

N = int(input().rstrip())
list_input = [0]*N
for i in range(N):
    list_input[i] = int(input().rstrip())

# # 버블 sort
# for i in range(1,N):
#     changed = False
#     for j in range(1,N - i):
#         if list_input[j] > list_input[j+1]:
#             changed = True
#             list_input[j], list_input[j+1] = list_input[j+1], list_input[j]

#     if changed == False:
#         print(i+1)
#         break


##시간 초과 => Why? O(N^2) => 25억번의 계산 시도가 일어남
##시간 초과가 일어나지 않게 하기 위해서는 
##버블 sort를 하지 않고 계산
## 정렬 전 후의 인덱스 차이를 계산하면 됨

idx = list(range(N))
##초기화 방식식
idx.sort(key = lambda i : list_input[i])
##람다식으로 내가 필요한 값을 받을 수 있음음
max_n = 0
for i in range(N):
    diff = idx[i] - i
    max_n = max(max_n, diff)

print(max_n+1)




