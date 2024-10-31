# 연산자 끼워넣기
import sys
input = sys.stdin.readline

answer=[]
def dfs(plus, minus, multi, div, value, count):
    global answer
    if count== n:
        answer.append(value)
        return

    if plus>=1:
        dfs(plus-1, minus, multi, div, value + a_list[count], count+1)
    if minus>=1:
        dfs(plus, minus-1, multi, div, value - a_list[count], count+1)
    if multi>=1:
        dfs(plus, minus, multi-1, div, value * a_list[count], count+1)
    if div>=1:
        if value < 0:
            value = -value
            dfs(plus, minus, multi, div-1, -(value // a_list[count]), count+1)
        else:
            dfs(plus, minus, multi, div-1, value // a_list[count], count+1)


n = int(input())
a_list = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
dfs(plus, minus, multi, div, a_list[0], 1)
print(max(answer))
print(min(answer))