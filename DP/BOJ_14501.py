# 퇴사(실버3)
# 1) 뒤에 기간 못채우는거 0으로 바꾼다.
# 2) 

n = int(input())
t=[]
p=[]
dp=[0] * (n+1)
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(1, n):
    time = t[i]
    profit = p[i]
    if i + time <= n:
        dp[i+time] = max(dp[i]+profit, dp[i+time])

    dp[i+1] = max(dp[i], dp[i+1])
print(dp[n])
