# 치킨배달
import sys
from itertools import combinations
input = sys.stdin.readline

def calDistance(chicken, house):
    c_x, c_y = chicken
    h_x, h_y = house
    return abs(c_x-h_x) + abs(c_y-h_y)

n, m = map(int, input().split())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))
house=[]
chicken=[]
for i in range(0, n):
    for j in range(0, n):
        if field[i][j]==2:
            chicken.append((i,j))
        elif field[i][j]==1:
            house.append((i,j))

chicken_c = list(combinations(chicken, m))
candidates=[]
for i in chicken_c:
    distances=0
    for h in house:
        min_house=999
        for j in i:
            min_house = min(min_house, calDistance(j,h))
        distances+=min_house
    candidates.append(distances)
print(min(candidates))