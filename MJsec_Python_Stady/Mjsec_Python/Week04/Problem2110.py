import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

##집의 갯수와 공유기 갯수
N, C = map(int,input().rstrip().split())

#리스트 컴프리헨션 => 집의 x_pos 잡기
house_positon = [int(input().rstrip()) for _ in range(N)]

house_positon.sort()

max_d = house_positon[-1] - house_positon [0]
min_d = 1
length = 0
while min_d <= max_d :
    mid = (max_d + min_d) // 2

    #거리에 따른 공유기 설치 가능 갯수 구하기 
    cnt = 1
    last_pos = house_positon[0]
    for i in range (1, N):
        if house_positon[i] - last_pos >= mid:
            cnt += 1
            last_pos = house_positon[i]
    
    if cnt >= C:
        length = mid
        min_d = mid + 1
    else:
        max_d = mid - 1


print(length)