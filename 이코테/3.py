# 문자열 뒤집기
s = input()
zero=0
one=0
before=''
for i in list(s):
    if i == before:
        continue
    if i=='0':
        zero+=1
        before = i
    else:
        one+=1
        before=i
print(min(zero, one))