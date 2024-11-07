# 고정점 찾기(이코테)
n = int(input())
array = list(map(int, input().split()))
start=0
end=n-1
answer=-1
while start <= end:
    middle = (start+end)//2
    if array[middle]==middle:
        answer=middle
        break
    elif array[middle] < middle:
        start=middle+1
    else:
        end=middle-1
print(answer)