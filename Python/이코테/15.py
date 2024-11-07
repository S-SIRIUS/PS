# 특정 거리의 도시 찾기
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    answer=[]
    queue= deque()
    queue.append((start, 0))
    visited[start]=True
    while queue:
        x, dist = queue.popleft()
        if dist==k:
            answer.append(x)
        
        for i in graph[x]:
            if visited[i]==False:
                visited[i]=True            
                queue.append((i, dist+1))
    
    return answer


n, m, k, x = map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
answer = bfs(x)
if len(answer)==0:
    print(-1)
else:
    print(*answer)
