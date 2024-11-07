# 동전1 (골드V)
n, k = map(int, input().split())
dp=[0]*(k+1)
coin=[]
for i in range(n):
    a = int(input())
    coin.append(a)
dp[0]=1
coin.sort()
print(dp)
for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp)
     