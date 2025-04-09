#슬라이싱 사용해서 풀기
import sys

input = sys.stdin.readline

input_s = input().rstrip()
search_s = input().rstrip()

i = 0
count = 0

while True:
    if i > len(input_s) - len(search_s):
        break

    if input_s[i : i + len(search_s)] == search_s:
        i += len(search_s)
        count += 1
    else:
        i +=1 

print(count)

# find 사용해서 풀기

# s.find("x", index) =>
# index를 기준값으로 찾아줌(return 값은 인덱스 // 해당하는 문자열이 존재하지 않을 시 -1)

# import sys

# input = sys.stdin.readline

# input_s = input().rstrip()
# search_s = input().rstrip()

# i = 0
# count = 0

# while True:
#     if i > len(input_s) - len(search_s):
#         break

#     if input_s.find(search_s, i) != -1:
#         i = input_s.find(search_s, i) + len(search_s)
#         count += 1
#     else:
#         i +=1 

# print(count)