# 볼링공 고르기
n, m = map(int, input().split())
ball = list(map(int, input().split()))
answer=0
for i in range(len(ball)):
    for j in range(i):
        if ball[i] != ball[j]:
            answer+=1
print(answer)