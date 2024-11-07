n = int(input())
scary = list(map(int, input().split()))
scary.sort()
count=0
answer=0
for i in scary:
    count+=1
    if count>=i:
        answer+=1
        count=0

print(answer)