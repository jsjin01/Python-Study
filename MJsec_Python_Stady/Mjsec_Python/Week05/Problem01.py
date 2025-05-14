import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs (graph, v , visited) :
    visited[v] = True
    global seq, seq_i
    seq[v] = seq_i
    seq_i += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

N, M ,R = map(int, input().rstrip().split())

input_arr =  [list(map(int,input().rstrip().split())) for _ in range(M)]
array = [[] for _ in range(N+1)]
seq = [0] * (N+1)
seq_i = 1

for arr in input_arr:
    array[arr[0]].append(arr[1])
    array[arr[1]].append(arr[0])

for n in range(1,N+1):
    array[n].sort()

visited = [False] * (N+1)
dfs(array,R,visited)

for i in range (1,N+1):
    print(seq[i])