import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().rstrip().split())

day = math.ceil((V - A) / (A - B)) + 1

print(day)
