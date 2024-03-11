# 카잉달력(실버1)
import sys
def inca(m, n, x, y): 
    k=x
    while(k <= m*n):      
        if ((k-x) % m==0) and ((k-y) % n==0):
            return k
        k+=m
    return -1
        
n = int(input())
for i in range(n):
    m, n, x, y = map(int, sys.stdin.readline().split())
    count  = inca(m,n,x,y)
    print(count)