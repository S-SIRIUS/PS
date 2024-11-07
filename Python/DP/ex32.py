# 정수삼각형(이코테)
import sys
input = sys.stdin.readline

n = int(input())
for i in range(0, n):
    triangle = list(map(int, input().split()))
    dp=triangle.copy()
    print(dp)
    if i!=0:
        for j in range(0, i+1):
            if j==0:
                dp[j] = before[j] + triangle[j]
            elif j==i:
                dp[j] = before[j-1] + triangle[j]
            else:
                dp[j] = max(before[j], before[j-1]) + triangle[j]
        
    before=dp.copy()
    print(before)
print(max(dp))

