# 바이러스(실버3)

import sys
sys.setrecursionlimit(10000)

ans = 0
def dfs(index):
    global ans
    global data
    if(check[index]==True):
        check[index]=False
        ans+=1
        for i in data[index]:
            dfs(i)

n = int(input())
pair = int(input())

data=[[] for _ in range(n+1)]
check = [True]*(n+1)

for i in range(pair):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
dfs(1)
print(ans-1)