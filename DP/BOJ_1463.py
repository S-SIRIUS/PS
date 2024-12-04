# 정수를 1로 만들기
n = int(input())
inf = int(1e9)
dp = [inf]*(n+1)

dp[1]=0
if(n>=2):
    dp[2]=1
if(n>=3):
    dp[3]=1
for i in range(1, n):
    current = i*3
    if current < n+1 and dp[current] > dp[i]+1:
        dp[current] = dp[i]+1
    current = i*2
    if current < n+1 and dp[current] > dp[i]+1:
        dp[current] = dp[i]+1
    current = i+1
    if current < n+1 and dp[current] > dp[i]+1:
        dp[current] = dp[i]+1
print(dp[n])