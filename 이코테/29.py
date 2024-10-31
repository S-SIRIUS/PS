# 공유기 설치
n, c = map(int, input().split())
array=[]
for i in range(n):
    array.append(int(input()))
array.sort()
start = 1
end = (array[-1] - array[0])
answer = 1

while start <= end:
    installation=1
    current_home = array[0]
    middle = (start + end) //2

    for i in range(1, n):
        if array[i] - current_home >= middle:
            current_home = array[i]
            installation+=1

    if installation >= c:
        start = middle+1
        answer = middle
    else:
        end = middle-1
print(answer)