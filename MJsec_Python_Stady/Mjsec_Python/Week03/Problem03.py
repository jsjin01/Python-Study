import sys
input  = sys.stdin.readline

N = int(input().rstrip())

student_list = []
for i in range(N):
    name, k, e, m = map(str, input().rstrip().split())
    student_list.append([name, int(k), int(e), int(m)])

# student_list = [["",0,0,0]]*N

# for i in range(N):
#     student_list[i] = list(input().rstrip().split())

sorted_student = sorted(student_list, key = lambda x : (-x[1] , x[2], -x[3], x[0]))


for i in range(N):
    print(sorted_student[i][0])