# 마인크래프트(실버2)
n, m, b = map(int , input().split())
table=[]
for i in range(0, n):
    table.append(list(map(int, input().split())))
minn=999
maxi=-999

for i in range(0, n):
    if minn > min(table[i]):
        minn = min(table[i])
    if maxi < max(table[i]):
        maxi = max(table[i])
anss_dic= {}
anss=[]

for i in range(minn, maxi+1):
    ans=0
    skeep=0
    bt= b
    for j in range(0, n):
        for k in range(0, m):
            if i > table[j][k]:
                if bt >= (i-table[j][k]):
                    ans += i-table[j][k]
                    bt-=(i-table[j][k])
                else:
                    skeep=1
            elif i < table[j][k]:
                if 256 >= bt+(table[j][k]):
                    ans += (table[j][k] - i)*2
                    bt+=(table[j][k]-i)
                else:
                    skeep=1
            if skeep==1:
                    break
        if skeep==1:
            break
    if(skeep!=1):
        anss.append(ans)
        anss_dic[ans] = i

print(min(anss), anss_dic[min(anss)])