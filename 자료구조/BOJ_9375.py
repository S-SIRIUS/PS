# 패션왕 신해빈(실버3)
n = int(input())
for i in range(n):
    hmap={}
    m = int(input())
    if m ==0:
        print(0)
    else:
        for j in range(m):
            a, b = map(str, input().split())
            if b in hmap:
                hmap[b]+=1
            else:
                hmap[b]=1
        
        if len(hmap) == 1:
            ans = m
            print(ans)
        else:
            ans2 = 1
            for i in hmap:
                ans2*= (hmap[i]+1)
            ans2
            print(ans2-1)