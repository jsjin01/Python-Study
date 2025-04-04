import sys
from collections import deque
input = sys.stdin.readline

dq = deque()

text = input().rstrip()
size = len(text)
left = 0
right = 0

for i in text:
    dq.append(int(i))

for i in range (int(size/2)):
        left += dq.popleft()
        right += dq.pop()


if(left == right):
      print("LUCKY")
else:
      print("READY")
    