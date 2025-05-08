import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

##집의 갯수와 공유기 갯수
N, C = map(int,input().rstrip().split())

#리스트 컴프리헨션 => 집의 x_pos 잡기
house_positon = [int(input().rstrip()) for _ in range(N)]

# 1 2 4 8 9
house_positon.sort()

# key point => 일정 거리 이상이 되면 설치를 해야됨 
# 그러면 기준이 되는 지점이 어떻게 나오는지 생각해봐야함
# 기준은 두점 사이의 최대값보다는 작고 최솟값보다는 큰 값이여야함 
# 총 거리를 C로 나눈 값보다 큰 수 중에서 가장 작은 좌표의 값을 설정

