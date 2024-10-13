# 여행계획(이코테)
import sys
input = sys.stdin.readline
def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b]=a
    else:
        parent[a]=b

n, m = map(int, input().split())
parent=[i for i in range(0, n+1)]
for i in range(1, n+1):
    graph = list(map(int ,input().split()))
    for j in range(0, n):
        if graph[j]==1:
            union(i,j+1)
travels = list(map(int, input().split()))

flag=True
standard=parent[travels[0]]
for travel in travels:
    if standard != parent[travel]:
        flag=False

if flag:
    print("YES")
else:
    print("NO")
