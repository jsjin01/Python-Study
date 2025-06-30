import sys
input = sys.stdin.readline

N = int(input().rstrip())
S = input().rstrip()
r = 31
M = 1234567891
problem_hash : int =0

#아스키코드 - 96
for i in range(N):
    problem_hash += ((ord(S[i])-96) * pow(r,i)) % M
    #해시한 값을 다시 해시 -> 정의
    problem_hash %= M
print(problem_hash)