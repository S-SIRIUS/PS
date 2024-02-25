# 좌표압축(실버2)
import sys
n = int(sys.stdin.readline())
coordinate = list(map(int, sys.stdin.readline().split()))
original = coordinate.copy()
coordinate.sort()
standard = coordinate[0]
temp=0
dic={}
dic[standard] = temp
for i in range(1, n):
    if(coordinate[i] > coordinate[i-1]):
        temp+=1
        dic[coordinate[i]] = temp
    else:
        dic[coordinate[i]] = temp
for i in original:
    print(dic[i], end=" ")
