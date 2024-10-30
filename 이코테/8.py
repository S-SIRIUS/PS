# 문자열 재정렬
data = list(input())
num=0
new_data=[]
for d in data:
    if ord('A') <=ord(d) <= ord('Z'):
        new_data.append(d)
        continue
    else:
        num+=int(d)
new_data.sort()
if num!=0:
    new_data.append(str(num))
print("".join(new_data))