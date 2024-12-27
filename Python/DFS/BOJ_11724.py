def dfs(now):
    visited[now]=True
    for i in graph[now]:
        if visited[i]==False:
            dfs(i)
    return
        

n, m = map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a, b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)
count=0
for i in range(1, n+1):
    if visited[i]==False:
        dfs(i)
        count+=1
print(count)