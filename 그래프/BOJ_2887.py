# 행성터널(플래5)
import sys
from itertools import combinations
input = sys.stdin.readline

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

def cruscal():
    planet_way.sort()
    answer=0
    for pw in planet_way:
        if find(pw[1]) != find(pw[2]):
            union(pw[1], pw[2])
            answer+=1
    return answer


n = int(input())
candidates = list(combinations([i for i in range(1, n+1)], 2))
planets=[()]
parent = [i for i in range(0, n+1)]

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((x,y,z))

planet_way=[]
for cd in candidates:
    distance = min(abs(planets[cd[0]][0]-planets[cd[1]][0]), abs(planets[cd[0]][1]-planets[cd[1]][1]),
                       abs(planets[cd[0]][2]-planets[cd[1]][2])) 
    planet_way.append((distance, cd[0], cd[1]))
    
print(cruscal())
