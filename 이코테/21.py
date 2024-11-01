# 인구이동
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]


def union(x, y):
    queue = deque()
    queue.append((x,y))

    union_list=[(x,y)]
    visited[x][y]=True

    total = field[x][y]
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<n and 0<=new_y<n and visited[new_x][new_y]==False and l<=abs(field[new_x][new_y]- field[x][y])<=r:
                union_list.append((new_x,new_y))
                count+=1
                total+=field[new_x][new_y]
                queue.append((new_x, new_y))
                visited[new_x][new_y]=True

    return union_list, total//count

def fill(u_list, data):
    for i in u_list:
        field[i[0]][i[1]] = data
    return        

n, l, r = map(int, input().split())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))
day=0
while True:
    visited=[[False]*(n) for _ in range(n)]
    flag=False
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                u_list, data = union(i,j)
                if len(u_list)>1:
                    flag=True
                    fill(u_list, data)
    if flag==False:
        break
    day+=1
print(day)