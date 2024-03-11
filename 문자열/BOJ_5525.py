#IOIOI(실버1)
def check(target, s, t_len, m):
    count=0
    i=0
    while i < m-t_len+1:
        if s[i] == target[0]:
            for j in range(1, t_len):
                if s[i+j] == target[j]:
                    if j == t_len-1:
                        count+=1
                        break
                    continue
                else:
                    i+=(j+1)
                    break
        i+=1                
    return count

n = int(input())
m = int(input())
s = input()
t_len = n*2+1
target=""
for i in range(t_len):
    if(i%2==1):
        target+="O"
    else:
        target+="I"
count = check(target, s, t_len, m)
print(count)