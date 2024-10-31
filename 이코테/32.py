# 정수삼각형
n = int(input())
before = False
dp=[]
for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, len(dp[i])):
        if j==0:
            dp[i][j] += dp[i-1][j]
        
        elif j==len(dp[i])-1:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[n-1]))