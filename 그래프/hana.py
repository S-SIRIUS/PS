# 공 옮기기
n = int(input()) # 컵의 개수
cup = list(map(int, input().split()))
m = int(input()) # 공 옮길 횟수
graph=[[]for _ in range(n+1)]
for i in range(m):
    x , y = map(int, input().split())
    cup[y-1] += cup[x-1]
    cup[x-1] = 0
print(cup)