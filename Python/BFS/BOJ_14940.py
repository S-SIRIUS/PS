#쉬운 최단거리(실버1)

from collections import deque

def bfs(x,y):
    global fields
    global check
    queue = deque()
    queue.append((x,y))
    fields[x][y]=0
    while queue:
        x, y = queue.popleft()
        check[x][y]=1
        dx=[1,0,0,-1]
        dy=[0,1,-1,0]

        for i in range(0, 4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if(new_x)>=0 and (new_x)<n and (new_y)>=0 and (new_y<m):
                if (fields[new_x][new_y]==1) and (check[new_x][new_y]==0):
                    fields[new_x][new_y] += fields[x][y]
                    queue.append((new_x, new_y))

n, m = map(int, input().split())
fields=[]
for i in range(0, n):
    fields.append(list(map(int, input().split())))

check=[[0 for _ in range(m)] for _ in range (n)]

for i in range(0, n):
    if(2 in fields[i]):
        target_x = i
        target_y = fields[i].index(2)
        break

bfs(target_x, target_y)

for i in range(0, n):
    for j in range(0, m):
        if (fields[i][j]==1) and (check[i][j]==0):
            fields[i][j]=-1   

for i in fields:
    print(*i)