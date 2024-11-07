# 연구소
import sys
import copy
from collections import deque
input = sys.stdin.readline
answer = []
dx = [-1, 1, 0, 0]
dy = [0 , 0, -1, 1]
def check(field):
    count=0
    for i in field:
        count+=i.count(0)
    return count

def extend(field):
    temp_field = copy.deepcopy(field)
    queue = deque()
    for i in range(n):
        for j in range(m):
            if temp_field[i][j]==2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<n and 0<=new_y<m and temp_field[new_x][new_y]==0:
                temp_field[new_x][new_y]=2
                queue.append((new_x, new_y))
    return temp_field


def makeWall(count):
    global answer
    if count == 3:
        new_field = extend(field)
        answer.append(check(new_field))
        return
    for i in range(0, n):
        for j in range(0, m):
            if field[i][j]==0:
                field[i][j]=1
                makeWall(count+1)
                field[i][j]=0

n, m = map(int, input().split())
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))
makeWall(0)
print(max(answer))