# 이코테(금광)
import sys
input = sys.stdin.readline


t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    temp=list(map(int, input().split()))
    field=[[] for _ in range(m)]
    for i in range(0, len(temp)):
        field[i % m].append(temp[i])
    
    print(field)
    dp=[[0]*n for _ in range(m)]
    
    for i in range(n):
        dp[0][i] = field[0][i]

    for i in range(1, m):
        for j in range(0, n):
            if j==0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j+1]) + field[i][j]
            
            elif j==n-1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + field[i][j]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + field[i][j]
    print(max(dp[m-1]))