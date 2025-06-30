import sys
input = sys.stdin.readline

#티셔츠 6종류 -> 같은 사이즈만 T장 묶음 / 부족X
#펜 -> P묶음or 1개 /딱뎀

N = int(input().rstrip())
T_array = list(map(int,input().rstrip().split()))
T, P = map(int,input().rstrip().split())

T_count = 0

for t in T_array:
    if t != 0:
        if t%T == 0:
            T_count += t//T
        else:
            T_count += t//T + 1

print(T_count)
print(f"{N//P} {N%P}")