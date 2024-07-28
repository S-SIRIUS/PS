import sys

answer=0
def dfs(S, T):
    global answer
    if T==S:
        answer = 1
        return
    if len(T) ==0:
        return
    if T[-1]=='A':
        dfs(S, T[:-1])
    if T[0] == 'B':
        dfs(S, T[1:][::-1])

# 입력
S = input().strip()
T = input().strip()

# 결과 출력
dfs(S, T)
print(answer)
