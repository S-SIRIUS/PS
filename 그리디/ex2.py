# 곱하기 혹은 더하기(이코테)
s = list(input())
answer=0
for i in s:
    i=int(i)
    if i<=1 or answer<=1:
        answer+=i
    else:
        answer*=i
print(answer)
