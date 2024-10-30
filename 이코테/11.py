# 뱀
from collections import deque
dx=[0, -1, 0, 1]
dy=[1, 0, -1, 0]

def change_direction(direction, c):
    if c=="L":
        if direction==3:
            direction=0
        else:
            direction+=1
    
    elif c=="D":
        if direction==0:
            direction=3
        else:
            direction-=1
    return direction


def snake():
    queue = deque()
    x = 0
    y = 0
    field[x][y]=-1
    queue.append((x,y))
    second=0
    direction=0
    
    while True:
        second+=1
        
        x += dx[direction]
        y += dy[direction]

        if x >=n or x<0 or y>=n or y<0 or field[x][y]==-1:
            return second
        
        if field[x][y]==1:
            field[x][y]=-1
        elif field[x][y]==0:
            del_x, del_y = queue.popleft()
            field[del_x][del_y]=0
            field[x][y]=-1
        queue.append((x,y))

        if direction_q and second==direction_q[0][0]:
            _, c = direction_q.popleft()
            direction = change_direction(direction, c)

n = int(input())
field = [[0]*(n) for _ in range(n)]

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    field[a-1][b-1]=1

l = int(input())
direction_q = deque()
for i in range(l):
    x, c = input().split() # 초 후에, c회전
    x = int(x)
    direction_q.append((x,c))
print(snake())
