# Z(실버1)
import sys
sys.setrecursionlimit(10000)

ans=0
def z_recur(n, x, y):
    global ans

    if(x==r) and (y==c):
        print(ans)
        exit(0)

    if(n==1):
        ans+=1
        return 0
    
    if not ((x<=r<=x+n) or (y<=c<=y+n)):
        ans+=n**2
        return 0

    # 1사분면
    z_recur(n//2, x, y)

    # 2사분면
    z_recur(n//2, x, y+n//2)

    # 3사분면
    z_recur(n//2, x+n//2, y)
    
    # 4사분면
    z_recur(n//2, x+n//2, y+n//2)

n, r, c = map(int, input().split())
z_recur(2**n, 0, 0)