import sys
from bisect import bisect_left,bisect_right

input = sys.stdin.readline

def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i,l_i

nums = [-1,-3,5,5,4,7,1,7,2,5,6]

nums.sort()
print(calCountsByRange(nums,5,7))