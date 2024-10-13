# 어두운 길(이코테)
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return

def cruscal():
    profit=0
    for edge in edges:
        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
        else:
            profit+=edge[0]

    return profit
n, m = map(int, input().split())
edges=[]
parent = [i for i in range(0, n+1)]
for i in range(m):
    n1, n2, cost = map(int, input().split())
    edges.append((cost, n1, n2))

edges.sort()
print(cruscal())