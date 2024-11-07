# 피보나치 함수(실버3)

cache=[[0 for _ in range(2)] for _ in range(41)]

cache[0][0] = 1
cache[0][1] = 0

cache[1][0] = 0
cache[1][1] = 1

for i in range(0, 39):
    cache[i+2][0] = cache[i+1][0] + cache[i][0]
    cache[i+2][1] = cache[i+1][1] + cache[i][1]

n=int(input())

for i in range(n):
    a = int(input())
    print(cache[a][0], cache[a][1])