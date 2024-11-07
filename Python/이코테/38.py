# 정확한 순위
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph=[[INF]*(n) for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1]=1

for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j]=0
            break

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
answer=0
for i in range(n):
    count=0
    for j in range(n):
        if graph[i][j]!=INF or graph[j][i]!=INF:
            count+=1
    if count==n:
        answer+=1
print(answer)