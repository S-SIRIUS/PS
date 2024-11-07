#듣보잡(실버4)
import sys
n, m = map(int, sys.stdin.readline().split())
n_listen=[]
n_see=[]
for i in range(n):
    n_listen.append(sys.stdin.readline().strip())
for i in range(m):
    n_see.append(sys.stdin.readline().strip())
ans = (set(n_listen)) & (set(n_see))

ans = list(ans)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])