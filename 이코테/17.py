# 경쟁적 전염
import sys
from collections import deque

input = sys.stdin.readline

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def extend(target_x, target_y):
    queue =[]
    for i in range(n):
        for j in range(n):
            if field[i][j]!=0:
                queue.append((field[i][j], i,j,0))
    queue = sorted(queue, key= lambda x: x[0])
    queue = deque(queue)
    while queue:
        virus, x, y, second = queue.popleft()
        
        if second == s:
            break
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<n and 0<=new_y<n and field[new_x][new_y]==0:
                field[new_x][new_y] = virus
                queue.append((virus, new_x, new_y, second+1))
    
    return field[target_x-1][target_y-1]


n, k = map(int, input().split())
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))
s, target_x, target_y = map(int, input().split())
print(extend(target_x, target_y))
