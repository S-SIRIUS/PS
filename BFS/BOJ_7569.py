from collections import deque
tomatoes=[]

def bfs(queue, tomatoes):
    global check
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while queue:
        x, y, z = queue.popleft()
        for i in range(0, 6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]

            #실제로 토마토가 익지 않았을때            
            if (0<= new_x <n) and (0<= new_y <m) and (0<= new_z <h) and (check[new_z][new_x][new_y]==0):
                if tomatoes[new_z][new_x][new_y] == 0:
                    tomatoes[new_z][new_x][new_y] = tomatoes[z][x][y] + 1
                    check[new_z][new_x][new_y] =  1
                    queue.append((new_x, new_y, new_z))

    max_value=-999
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatoes[k][i][j]==0:
                    return -1
                elif tomatoes[k][i][j] > max_value:
                    max_value = tomatoes[k][i][j]
    return max_value-1

m, n, h = map(int, input().split())
queue = deque()
check=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

for k in range(h):
    tomato=[]
    for i in range(n):
        tomato.append(list(map(int, input().split())))
    tomatoes.append(tomato)

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomatoes[k][i][j]==1:
                queue.append((i,j,k))
                check[k][i][j] = 1
max_ans = bfs(queue, tomatoes)
print(max_ans)
