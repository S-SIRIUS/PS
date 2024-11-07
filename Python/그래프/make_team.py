# 팀결성(이코테)
def find(x):
    if parent[x] != x:
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
for i in range(m):
    o, s1, s2 = map(int, input().split())

    if o==0:
        union(s1, s2)
    else:
        if find(s1) == find(s2):
            print("YES")
        else:
            print("NO")


