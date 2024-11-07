# 곱하기 혹은 더하기
s = list(input())
answer=0
for i in range(0, len(s)):
    if int(s[i])==0 or int(s[i])==1 or answer==0:
        answer+=int(s[i])
    else:
        answer*=int(s[i])
print(answer)