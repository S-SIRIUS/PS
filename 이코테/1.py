# 모험가 길드
n = int(input())
scary = list(map(int, input().split()))
scary.sort()
count=0
group=0
for i in scary:
    count+=1
    if count >=i:
        group+=1
        count=0
print(group)