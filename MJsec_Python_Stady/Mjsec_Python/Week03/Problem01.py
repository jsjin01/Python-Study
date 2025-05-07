import sys
input = sys.stdin.readline

N = int(input().rstrip())
list_index = [0]*1000001
for i in range(N):
    num = int(input().rstrip())
    list_index[num] += 1

for i in range(len(list_index)):
    if list_index[i] != 0:
        for j in range (list_index[i]):
            print(i)


## enumerate() 함수 => for 문에서 많이 사용
## 2개의 값 반환 => index 와 안에 들어간 값
## for index, i in  enumerate(array) => 예시