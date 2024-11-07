# 테트로미토(골드4)
def dfs(x,y, summ, count):
    if count==4:
        value.append(summ)
        return
    if(x+1>=0 and x+1<n and y>=0 and y<m and visited[x+1][y]==False):
        visited[x+1][y]=True
        dfs(x+1, y, summ+field[x+1][y], count+1)
        visited[x+1][y]=False
    if(x-1>=0 and x-1<n and y>=0 and y<m and visited[x-1][y]==False):
        visited[x-1][y]=True
        dfs(x-1, y, summ+field[x-1][y], count+1)
        visited[x-1][y]=False
    if(y+1>=0 and y+1<m  and x>=0 and x<n and visited[x][y+1]==False):
        visited[x][y+1]=True
        dfs(x, y+1, summ+field[x][y+1], count+1)
        visited[x][y+1]=False
    if(y-1>=0 and y-1<m and x>=0 and x<n and visited[x][y-1]==False):
        visited[x][y-1]=True
        dfs(x,y-1, summ+field[x][y-1], count+1)
        visited[x][y-1]=False
    return

def etc(x, y):
    if(x+2>=0 and x+2<n):
        summ=0
        summ+=field[x][y] + field[x+1][y] + field[x+2][y]
        if(y+1>=0 and y+1<m):
            summ1=summ+field[x+1][y+1]
            value.append(summ1)
        if(y-1>=0 and y-1<m):
            summ2=summ+field[x+1][y-1]
            value.append(summ2)
    if(x-2>=0 and x-2<n):
        summ=0
        summ+=field[x][y] + field[x-1][y] + field[x-2][y]
        if(y+1>=0 and y+1<m):
            summ1=summ+field[x-1][y+1]
            value.append(summ1)
        if(y-1>=0 and y-1<m):
            summ2=summ+field[x-1][y-1]
            value.append(summ2)
    if(y+2>=0 and y+2<m):
        summ=0
        summ+=field[x][y] + field[x][y+1] + field[x][y+2]
        if(x+1>=0 and x+1<n):
            summ1=summ+field[x+1][y+1]
            value.append(summ1)
        if(x-1>=0 and x-1<n):
            summ2=summ+field[x-1][y+1]
            value.append(summ2)
    if(y-2>=0 and y-2<m):
        summ=0
        summ+=field[x][y] + field[x][y-1] + field[x][y-2]
        if(x+1>=0 and x+1<n):
            summ1=summ+field[x+1][y-1]
            value.append(summ1)
        if(x-1>=0 and x-1<n):
            summ2=summ+field[x-1][y-1]
            value.append(summ2)
        


n, m = map(int, input().split())
field=[]
visited=[[False]*m for _ in range(n)]
for i in range(n):
    field.append(list(map(int, input().split())))

value=[]
for i in range(0, n):
    for j in range(0, m):
        visited[i][j] = True
        dfs(i,j,field[i][j], 1)
        visited[i][j] = False
        etc(i,j)
print(max(value))
