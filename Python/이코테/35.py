# 못생긴 수
n = int(input())
ugly=[1]
num=2
while len(ugly) <= n-1:
    if num %2 ==0 or num%3==0 or num%5==0:
        ugly.append(num)
    num+=1
print(ugly[n-1])