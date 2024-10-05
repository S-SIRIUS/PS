# 숨바꼭질 3 (골드5)
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue= deque()
    queue.append(n)
    visited[n]=0
    while queue:
        subin = queue.popleft()
        if subin == k:
            return visited[subin]
        
        if 0<=(subin*2)<=100000 and visited[subin*2]==-1:
            queue.appendleft(subin*2)
            visited[subin*2]=visited[subin]
            
        if 0<=(subin-1) <= 100000 and visited[subin-1]==-1:
            queue.append(subin-1)
            visited[subin-1]=visited[subin]+1

        if 0<=(subin+1)<=100000 and visited[subin+1]==-1:
            queue.append(subin+1)
            visited[subin+1]=visited[subin]+1
  
n, k = map(int, input().split())
visited=[-1]*(100001)
print(bfs())
