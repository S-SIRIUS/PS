# 플로이드
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())

graph=[[INF]*(n) for _ in range(n)]
for i in range(m):
    start, end, cost = map(int, input().split())
    if graph[start-1][end-1] !=0:
        graph[start-1][end-1] = min(graph[start-1][end-1], cost)
    else:
        graph[start-1][end-1] = cost

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j]=0
            continue

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in graph:
    print(*i)