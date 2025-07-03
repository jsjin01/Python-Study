import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    H, W ,N = map(int, input().rstrip().split())

    # 층수 계산
    h = N % H
    
    if h == 0:
        h = H
        w = N // H
    else:
        w = N // H + 1

    # 호수를 두 자리 문자열로 만들기
    room = str(h) + (f"{w:02}")
    print(room)
