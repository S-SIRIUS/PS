
import sys
sys.setrecursionlimit(10000)
def dfs(x, y, graph, visited, threshold):
    if x>=0 and x<n and y>=0 and y<n and visited[x][y]==False and graph[x][y] > threshold:
            visited[x][y] = True
            dfs(x+1, y, graph, visited, threshold)
            dfs(x, y+1, graph, visited, threshold)
            dfs(x, y-1, graph, visited, threshold)
            dfs(x-1, y, graph, visited, threshold)

    return




n = int(input())
graph=[]
visited=[[False]*n for _ in range(n)]
max_value=0
for i in range(n):
    graph.append(list(map(int, input().split())))
    if max_value < max(graph[i]):
         max_value = max(graph[i])

all=[]
for i in range(max_value):
    count=0
    for j in range(n):
        for k in range(n):
            if visited[j][k]==False and graph[j][k] > i:
                count+=1
                dfs(j, k, graph, visited, i)
    all.append(count)

    visited= [[False]*n for _ in range(n)]
print(max(all))


    