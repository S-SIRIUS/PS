#색종이 만들기(실버2)
white=0
blue=0

def cutting(n, x, y):
    global white
    global blue
    global paper

    if(n==1):
        if paper[x][y]==0:
            white += 1
        else:
            blue += 1
        return
    else:
        temp = paper[x][y]
        result=0
        for i in range(x, x+n):
            for j in range(y, y+n):
                if(temp != paper[i][j]):
                    result=1
                    break
        if(result == 1):
            cutting(n//2, x, y)
            cutting(n//2, x, y+n//2)
            cutting(n//2, x+n//2, y)
            cutting(n//2, x+n//2, y+n//2)
        else:
            if temp == 0:
                white+=1
            else:
                blue+=1

n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

cutting(n, 0, 0)
print(white)
print(blue)