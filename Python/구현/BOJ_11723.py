#집합(실버5)
import sys
group=set()
def cal(exp, num):
    global group
    if((num!=None) and (num>=1) and (num<=20)):
        if exp == "add":
            if(num not in group):
                group.add(num)
        elif exp == "remove":
            if(num in group):
                group.remove(num)
        elif exp == "check":
            if(num in group):
                sys.stdout.write(str(1)+'\n')
            else:
                sys.stdout.write(str(0)+'\n')
        elif exp == "toggle":
            if(num in group):
                group.remove(num)
            else:
                group.add(num)

    elif exp == "all":
        group = set([i for i in range(1, 21)])
    
    elif exp == "empty":
        group = set()
        
n = int(input())
for i in range(0, n):
    exp = sys.stdin.readline().split()
    if(len(exp)==2):
        cal(exp[0], int(exp[1]))
    else:
        cal(exp[0], None)

