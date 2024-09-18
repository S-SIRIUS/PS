# 거짓말(골드 4)
trueman_dic = {}
n, m = map(int, input().split())
answer=m
input_data=[]
for i in range(1, n+1):
    trueman_dic[i]=0
trueman = list(map(int, input().split()))
if len(trueman)==1:
    for i in range(m):
        party = list(map(int, input().split()))
else:
    trueman = trueman[1:]
    for i in trueman:
        trueman_dic[i]=1

    for i in range(m):
        party = list(map(int, input().split()))[1:]
        input_data.append(party)
        retry=0
        for p in party:
            if trueman_dic[p]==1:
                retry=1
                break

        if retry==1:
            for p in party:
                trueman_dic[p]=1

for i in input_data:
    for j in i:
        if trueman_dic[j]==1:
            answer-=1
            break
print(answer)