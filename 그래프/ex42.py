# 탑승구(이코테)
def find(x):
    if x!=parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())
parent=[i for i in range(0, g+1)]
answer=0
for i in range(p):
    info = int(input())
    if find(info) == info:
        union(info, info-1)
        answer+=1
    else:
        continue
print(answer)
