# 치킨배달(골드5)
from itertools import combinations
import sys
input= sys.stdin.readline

def choose_short(candidate):
    global house
    global minimum_candidate
    minimum=1e9
    summ=0
    for j in house:
        minimum=1e9
        for i in candidate:
            value = abs(i[0] - j[0]) + abs(i[1]-j[1])
            if value < minimum:
                minimum=value
        summ+=minimum
    minimum_candidate.append(summ)
    return
    
n, m = map(int, input().split())
field=[]
chicken=[]
house=[]
for i in range(n):
    field.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if field[i][j]==2:
            chicken.append((i,j))
        elif field[i][j]==1:
            house.append((i,j))
minimum_candidate=[]
candidates = list(combinations(chicken, m))
for candidate in candidates:
    choose_short(candidate)
print(min(minimum_candidate))





'''
chicken={}
house=[]
def make_data():
    for i in range(n):
        for j in range(n):
            if field[i][j] == 2:
                chicken[(i,j)] = []
            elif field[i][j] == 1:
                house.append((i,j))

def short_appendTo_chicken():
    global chicken

    for i in house:
        x, y = i
        minimum=99999999
        for key in chicken:
            chicken_x, chicken_y = key
            value = (abs(x-chicken_x) + abs(y-chicken_y))
            if (value) < minimum:
                minimum=value
                minimum_key=(chicken_x, chicken_y)
        chicken[minimum_key].append(minimum)
    return

def delete():
    global chicken
    answer=0
    chicken = sorted(chicken.items(), key = lambda x: (len(x[1]), sum(x[1])))
    if m > len(chicken): # 폐업안시켜도 될때
        start = 0
    else:
        start = len(chicken) - m

    print(chicken)
    for i in range(start, len(chicken)):
        answer+=sum(chicken[i][1])
    return answer

n, m = map(int, input().split())
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))

make_data()
short_appendTo_chicken()
print(delete())
'''