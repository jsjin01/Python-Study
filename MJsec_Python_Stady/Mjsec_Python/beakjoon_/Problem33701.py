import sys
import random as rd
input = sys.stdin.readline

# 마지막 gwan ->  맨 앞 글자는 n
# 최대 45의 알파벳을 뽑기

a = 'abcdefghijklmnopqrstuvxyz'
s= ["n"]

n = rd.randrange(2,46)

for i in range(n):
    m = rd.randrange(0,25)
    s.append(a[m])

k = rd.randrange(1,n)
u = rd.randrange(1,n)

s[k] = "k"
s[u] = "u"

for l in "gwan":
    s.append(l)

st = ""
for i in s:
    st += i

print(st)