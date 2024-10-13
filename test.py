import sys
input = sys.stdin.readline

dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]


def way_change(way):
    
    way+=1
    if way>=4:
        way=0
    return way


n = int(input())
field=[[-1]*(n) for _ in range(n)]
x=0
y=0
way=0

for i in range(0, n*n):
    field[x][y]=i
    print(i)
    new_x = x+dx[way]
    new_y = y+dy[way]
    if new_x < 0 or new_x>=n or new_y<0 or new_y>=n or field[new_x][new_y]!=-1:
        way = way_change(way)
    
    x +=dx[way]
    y +=dy[way]

print(field)