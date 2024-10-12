# 문자열 재정렬(이코테)
s = list(input())
s.sort()
integer=0
for i in range(0, len(s)):
    if ord(s[i]) <=57:
        integer += int(s[i])
    else:
        break
print(integer)
print("".join(s[i:len(s)])+ str(integer))
