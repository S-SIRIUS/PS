#AC(골드5)

from collections import deque
import sys

def check_p(p, g):
    queue = deque(g)
    r_count= 0

    for i in p:
        if i == 'R':
            r_count+=1
        elif i == 'D':
            if not queue:
                print("error")
                return
            if(r_count%2==1):
                queue.pop()
            else:
                queue.popleft()
    if(r_count%2==1):
        queue.reverse()
    print(str(list(queue)).replace(" ", ""))
    return

t = int(sys.stdin.readline())
for i in range(t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    g = sys.stdin.readline().strip().replace('[','').replace(']','').split(',')
    if(n==0):
        g=[]
    else:
        g = list(map(int, g))

    check_p(p,g)
