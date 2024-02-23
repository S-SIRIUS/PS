# 나는야 포켓몬 마스터 이다솜(실버4)
import sys

n, p_num = map(int, sys.stdin.readline().split( ))
pokemon={}
for i in range(0, n):
    name = sys.stdin.readline().strip()
    pokemon[str(i+1)] = name 
    pokemon[name] = i+1

for i in range(0, p_num):
    print(pokemon[sys.stdin.readline().strip()])