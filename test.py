import sys
sys.setrecursionlimit(10**7)

answer=0
cases=[1, 2]
def dfs(total, n):
    global answer
    global cases
    
    if total==n:
        answer+=1
        return
    elif total>n:
        return
    else:
        for i in cases:
            dfs(total + i, n)

n = int(input())
for case in cases:
    dfs(case, n)  
print(answer % 1234567)