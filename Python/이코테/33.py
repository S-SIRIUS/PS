# 퇴사
n = int(input())
t=[]
p=[]
for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
dp = [0]*(n+1)


for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i]+ dp[time], dp[i])

print(max(dp))