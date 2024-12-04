# 못생긴 수(이코테)
n = int(input())
dp=[1]*(1001)
index_2, index_3, index_5 = 0
two, three, five = 2, 3, 5
for i in range(1, n+1):
    dp[i] = min(two, three, five)

    


    


