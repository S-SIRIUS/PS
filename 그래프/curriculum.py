# 커리큘럼(이코테)
from collections import deque
v = int(input())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]
time = [0]*(v+1)
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = time.copy()
    queue = deque()

    for i in range(1, v+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        now =queue.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i]-=1

            if indegree[i]==0:
                queue.append(i)
    for i in range(1, v+1):
        print(result[i])
topology_sort()