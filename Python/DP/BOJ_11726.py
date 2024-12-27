# 2*N 타일 채우기(실버3)
import sys
input = sys.stdin.readline
n = int(input())
dp=[0]*(1001)
dp[1]=1
dp[2]=2
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])