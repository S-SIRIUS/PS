# 효율적인 화폐 구성(이코테 기본)
n, m = map(int, input().split())
coins=[]
for i in range(n):
    coins.append(int(input()))

dp=[999]*(m+1)
for coin in coins:
    dp[coin]=1

for i in range(n):
    for coin in coins:
        dp[i+coin] = min(dp[i]+1, dp[i+coin])