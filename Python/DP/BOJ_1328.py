# 빌딩 순서 구하기
import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
dp = [[[0]*(r+1) for _ in range(l+1)] for _ in range(n+1)]
dp[1][1][1]=1

for i in range(2, n+1):
    for j in range(1, l+1):
        for k in range(1, r+1):
            dp[i][j][k] = (dp[i-1][j][k-1] + dp[i-1][j-1][k] + dp[i-1][j-1][k-1]*(i-2)) % 1000000007
print(dp[n][l][r])