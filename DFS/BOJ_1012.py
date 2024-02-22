import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    global field

    if(field[x][y]==1):
        field[x][y]=-1
        if(x+1<n) and (x+1>=0):
            dfs(x+1, y)
        if(x-1<n) and (x-1>=0):
            dfs(x-1, y)
        if(y+1<m) and (y+1>=0):
            dfs(x, y+1)
        if(y-1<m) and (y-1>=0):
            dfs(x, y-1)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    return 0

t = int(input())
for i in range(t):
    ans=0
    m, n, k = map(int, input().split())
    field=[[0 for _ in range (m)] for _ in range(n)]
    for j in range(k):
        x, y =map(int, input().split())
        field[y][x] = 1

    for i in range(n):
        for j in range(m):
            if(field[i][j] == 1):
                dfs(i, j)
                ans+=1
    print(ans)