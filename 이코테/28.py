# 고정점 찾기
n = int(input())
array = list(map(int, input().split()))
start = 0
end = len(array)
while start <= end:
    middle = (start + end) //2
    if middle == array[middle]:
        print(middle)
        break
    elif middle > array[middle]:
        start = middle
    else:
        end=middle


