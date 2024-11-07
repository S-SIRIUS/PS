# 병사 배치하기
n = int(input())
soldiers = list(map(int, input().split()))
soldiers = soldiers[::-1]
dp=[1]*(n)
for i in range(1, n):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(n-max(dp))