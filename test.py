n, m = map(int, input().split())
fields=[]
fields.append(list(map(int, input().split())))
for i in range(0, n):
    if(2 in fields[i]):
        target_x = i
        target_y = fields[i].index(2)
        break
print(target_x, target_y)