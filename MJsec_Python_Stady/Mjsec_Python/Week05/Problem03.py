import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def bfs (graph, node , visited) :
    queue = deque([node])
    visited[node] = True
    distance = [0] * len(graph)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1
    
    return distance

N, M, K, X = map(int, input().rstrip().split())

connection = [list(map(int, input().rstrip().split())) for _ in range (M)]

city =[[] for _ in range (N+1)]

for arr in connection:
    city[arr[0]].append(arr[1])

for n in range(1,N+1):
    city[n].sort()

visited = [False] * (N+1)
dist = bfs(city , X, visited)
cnt = 0

for i in range (1, N+1):
    if dist[i] == K:
        cnt += 1
        print(i)
if cnt == 0:
    print(-1)
    



